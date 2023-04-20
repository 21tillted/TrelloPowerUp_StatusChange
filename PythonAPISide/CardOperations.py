import config
import requests
from trello import TrelloClient
from ProDemote import *

class CardOperations:

    client = TrelloClient(
      api_key= config.__myApi_key__,
      api_secret= config.__myApi_secret__,
      token= config.__myToken__,
      #token_secret='your-oauth-token-secret'
    )
    
    #sort the given card to the righ position
    def sortin_card(self, card):
        currentBoard = self.client.get_board(config.__boardid__)
        all_lists = currentBoard.open_lists()
        

        for currentList in all_lists[1:]:     #später [1:] machen um die standartdaten zu übersprüngen
            for currentCard in currentList.list_cards():
                if currentCard.labels.__contains__(f'{card.labels[0]}'):
                    self.move_card(card_id=card.id, idList=currentList.id, listPos=currentCard.id+1)
                    return


    #move a card on board
    def move_card(self, card_id, idList=None, listPos=None):
        url = f"https://api.trello.com/1/cards/{card_id}"

        card_id
        headers = {
            "Accept": "application/json"
        }

        query ={}
        if idList != None and listPos == None:
            query = {
                'key': config.__myApi_key__,    
                'token': config.__myToken__,
                'idList': idList
            }
        elif idList == None and listPos != None:
            query = {
                'key': config.__myApi_key__,    
                'token': config.__myToken__,
                'pos': listPos
            }
        else:
            query = {
                'key': config.__myApi_key__,    
                'token': config.__myToken__,
                'idList': idList,
                'pos': listPos
            }

        response = requests.put(url,headers=headers,params=query)

        return response


    #exchange one label for another label(Rank)
    def change_label_of_card(self,card_id, oldRank, newRank):
        addingResponse = self.remove_label_from_card(card_id, oldRank) 
        removalResponse = self.add_label_to_card(card_id, newRank)

        if addingResponse != '400' or removalResponse != '400':
            return f'adding: {addingResponse}, removing: {removalResponse}'
        

    #remove a label from a card
    def remove_label_from_card(self, card_id, rank):                            #Rank is String to be able to compare to the dict
        label_id = config.__rankLabels__[rank]                                #get the label refaring to the Rank from the config as string
        url = f"https://api.trello.com/1/cards/{card_id}/idLabels/{label_id}" #API url

        query = {
            'key': config.__myApi_key__,    
            'token': config.__myToken__
        }

        response = requests.delete(url, params=query)

        return response


    #add a label to a card
    def add_label_to_card(self, card_id, rank):                   #Rank is String to be able to compare to the dict
        url = f"https://api.trello.com/1/cards/{card_id}/idLabels"  #API url
        label_id = config.__rankLabels__[rank]                      #get LabelID for rank from dicturnary

        query = {
            'key': config.__myApi_key__,
            'token': config.__myToken__,
            'value': label_id
        }

        response = requests.post(url, params=query)

        return response  
import config
import requests
from trello import TrelloClient
from trello import List, Card
from ProDemote import *
from datetime import date
import json

class CardOperations:

    client = TrelloClient(
      api_key= config.__myApi_key__,
      api_secret= config.__myApi_secret__,
      token= config.__myToken__,
      #token_secret='your-oauth-token-secret'
    ) 
    
    #sort the given card to the righ position
    def sortin_card(self, card, destinationRank):
        currentBoard = self.client.get_board(config.__boardid__)
        all_lists = currentBoard.open_lists()
        

        for currentList in all_lists[1:]:     #später [1:] machen um die standartdaten zu übersprüngen
            for currentCard in currentList.list_cards():
                if currentCard.name.startswith(f'[{destinationRank}]'):
                    responsecode = self.move_card(card_id=card.id, idList=currentList.id, listPos=currentCard.pos+1)
                    if responsecode != 200:
                        response = f'{responsecode}\n'
                        return response
                    else:
                        return ''


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

        return response.status_code


    #exchange one label for another label(Rank)
    def change_label_of_card(self,card_id, oldRank, newRank):
        removalResponse = self.remove_label_from_card(card_id, oldRank) 
        addingResponse = self.add_label_to_card(card_id, newRank)

        if addingResponse != 200 or removalResponse != 200:
            return f'adding: {addingResponse}, removing: {removalResponse}'
        else:
            return ''
        

    #remove a label from a card
    def remove_label_from_card(self, card_id, rank):                            #Rank is String to be able to compare to the dict
        label_id = config.__rankLabels__[rank]                                #get the label refaring to the Rank from the config as string
        url = f"https://api.trello.com/1/cards/{card_id}/idLabels/{label_id}" #API url

        query = {
            'key': config.__myApi_key__,    
            'token': config.__myToken__
        }

        response = requests.delete(url, params=query)

        return response.status_code


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

        return response.status_code  
    

    #edit custom field
    def edit_Promote_Sperre(self, card, newRank):
        customfield = card.get_custom_field_by_name('Promote Sperre bis:')

        url = f"https://api.trello.com/1/cards/{card.id}/customField/{customfield.id}/item"

        headers = {
        "Content-Type": "application/json"
        }

        query = {
        'key': f'{config.__myApi_key__}',
        'token': f'{config.__myToken__}'
        }

        payload = json.dumps( {
        "value": {
            "date": "2018-03-13T16:00:00.000Z",
            }
        } )


        response = requests.put(url,data=payload,headers=headers,params=query)  

        if config.__ranks__.index(f'{newRank}') < config.__ranks__.index('SGT'):
            #promotesperre +2 Tage
            card.set_custom_field(self, date.today, customfield)
        
            return
        elif config.__ranks__.index(f'{newRank}') < config.__ranks__.index('SLT'):
            #promotesperre +7 Tage
            card.set_custom_field(self, date.today+7, customfield)
            return
        else: 
            #promotesperre +14Tage
            card.set_custom_field(self, date.today+14, customfield)
            return
        

        #card.set_custom_field(self, value, customfield)

    def new_card(self, userSteamID, listID, name):
        url = "https://api.trello.com/1/cards"
        ID = userSteamID
        headers = {
        "Accept": "application/json"
        }

        query = {
        'idList': f'{listID}',
        'key': f'{config.__myApi_key__}',
        'token': f'{config.__myToken__}',
        'name': f'{name}'
        }

        response = requests.put(
        url,
        headers=headers,
        params=query
        )

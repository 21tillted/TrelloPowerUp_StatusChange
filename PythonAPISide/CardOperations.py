import config
import requests 


class CardOperations:

    #move a card on board
    def move_card(self, card, destinationList, destinationIndex):
        return


    #exchange one label for another label(Rank)
    def changeLabelOfCard(self,card_id, oldRank, newRank):
        
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
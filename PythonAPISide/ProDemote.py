from trello import TrelloClient
from trello.customfield import CustomField, CustomFieldText, CustomFieldCheckbox, CustomFieldNumber, CustomFieldDate, CustomFieldList
import config
import requests

class ProDemote:

  client = TrelloClient(
      api_key= config.__myApi_key__,
      api_secret= config.__myApi_secret__,
      token= config.__myToken__,
      #token_secret='your-oauth-token-secret'
  )

  def getCardFromSteamID(self, steamID):
    currentBoard = self.client.get_board(config.__boardid__)
    print(currentBoard.name) ##justTest case
    # Get all the list in the board 
    all_lists = currentBoard.open_lists() 
    
    # Get all relevant Lists and Cards
    for currentlist in all_lists[1:]:     #später [1:] machen um die standartdaten zu übersprüngen
      for currentcard in currentlist.list_cards():
        CardData = {}

        #find corresponding card for the SteamID
        if not currentcard.name.__contains__('-'):

          #Get the custom fields
          for custom_fields in currentcard.custom_fields: 
            CardData[custom_fields.name]= [custom_fields.value]
          
          if CardData.get['SteamID'] != None and CardData['SteamID'] == steamID:
            return currentcard
    return "Card not found"
            

  ###WORK IN PROGRESS
  #get only name and Rank for the ProDemote form
  def getNameAndRankFromSteamID(self, steamID):
    targetCard = self.getCardFromSteamID(steamID)

    #for label in __selectedCard__.

    #return f'Name: {__selectedCard__.name}\nVom Rang: {}'


  #return every Data of a User
  def getDataOfUser(self, steamID):
    targetCard = self.getCardFromSteamID(steamID)

    CardData = {} #where to save the Data of the fields

    for custom_fields in targetCard.custom_fields: 
        
        # Get the custom fields Data
        for custom_fields in targetCard.custom_fields: 
          CardData[custom_fields.name]= [custom_fields.value]

    return CardData
  
  
  ##WORK IN PROGRESS#promote or demote a user
  def proDemoteUser(self, steamID, comment):  
    targetCard = self.getCardFromSteamID(steamID)
    ErrorMessage = self.changeLabelOfCard(targetCard, )    ###comment will be a discturnary, where we get the oldRank and new Rank from
    #sort
    self.makePromDemComment(steamID, comment)

    if ErrorMessage != '':
      return ErrorMessage


  #changeLabel(Rank)
  def changeLabelOfCard(self,card_id, oldRank, newRank):
    
    addingResponse = self.remove_label_from_card(card_id, oldRank) 
    removalResponse = self.add_label_to_card(card_id, newRank)

    if addingResponse != '400' or removalResponse != '400':
      return f'adding: {addingResponse}, removing: {removalResponse}'
    

  #remove a label from a card
  def remove_label_from_card(self, card_id, rank):                        #Rank is String to be able to compare to the dict
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


  #Comment the approved Promote under the card of the user
  def makePromDemComment(self, steamID, comment):  #Comment has to be formated as dictunary
    targetCard = self.getCardFromSteamID(steamID)

    targetCard.comment(f'Wer: {comment[0]}\nVon wem: {comment[1]}\nRang: [{self.__selectedCard__.getLabel}]->[{comment[3]}]\nGrund: {comment[4]}\nDatum: {comment[5]}\nSteamID: {steamID}') ##steamID is implicit (nedded to find card)
  

  #Comment the approved positive or negative 
  def makePoNeComment(self, steamID, comment):  #Comment has to be formated as dictunary 
    targetCard = self.getCardFromSteamID(steamID)

    targetCard.comment(f'Wer: {comment[0]}\nVon wem: {comment[1]}\nGrund: {comment[2]}\n\nDatum: {comment[3]}\nSteamID: {steamID}') ##steamID is implicit (nedded to find card)
  
  




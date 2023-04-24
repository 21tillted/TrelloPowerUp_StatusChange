from trello import TrelloClient
from trello.customfield import CustomField, CustomFieldText, CustomFieldCheckbox, CustomFieldNumber, CustomFieldDate, CustomFieldList
import config
from CardOperations import * 

class ProDemote:
  
  client = TrelloClient(
      api_key= config.__myApi_key__,
      api_secret= config.__myApi_secret__,
      token= config.__myToken__,
      #token_secret='your-oauth-token-secret'
  )
  co = CardOperations()


  #get  a card by steamID
  def getCardFromSteamID(self, steamID):
    currentBoard = self.client.get_board(config.__boardid__)

    # Get all the list in the board 
    all_lists = currentBoard.open_lists() 
    
    # Get all relevant Lists and Cards
    for currentList in all_lists[1:]:     #später [1:] machen um die standartdaten zu übersprüngen
      for currentCard in currentList.list_cards():
        CardData = {}

        #find corresponding card for the SteamID
        if '-' not in currentCard.name and not currentCard.name.startswith('['):

          #Get the custom fields
          for custom_fields in currentCard.custom_fields: 
            CardData[custom_fields.name]= [custom_fields.value]
          
          if CardData.get('SteamID') != None and CardData.get('SteamID')[0] == steamID:
            return currentCard
          
    return "Card not found"
            

  ###WORK IN PROGRESS
  #get only name and Rank for the ProDemote form
  def getNameAndRankFromSteamID(self, steamID):
    targetCard = self.getCardFromSteamID(steamID)
    name = targetCard.name
    rank = targetCard.labels[0]
    
    return f'Name: {targetCard.name}\nVom Rang: {rank.name}'


  #return every Data of a User
  def getDataOfUser(self, steamID):
    targetCard = self.getCardFromSteamID(steamID)

    CardData = {} #where to save the Data of the fields

    for custom_fields in targetCard.custom_fields: 
        
        # Get the custom fields Data
        for custom_fields in targetCard.custom_fields: 
          CardData[custom_fields.name]= [custom_fields.value]

        CardData['Rank'] = [config.__rankLabels__[targetCard.labels[0]]]
    return CardData
  
  
  ##WORK IN PROGRESS#promote or demote a user
  def proDemoteUser(self, steamID, comment):  
    ErrorMessage = ''
    targetCard = self.getCardFromSteamID(steamID)
    
    ErrorMessage += self.co.sortin_card(card=targetCard,destinationRank=comment[3])           #sort the card in the right place on board
    ErrorMessage += self.co.change_label_of_card(card_id=targetCard.id, oldRank= comment[2], newRank=comment[3])    ###comment will be a dictionary, where we get the oldRank and new Rank from
    self.co.edit_Promote_Sperre(card=targetCard, newRank=comment[3])
    
    self.makePromDemComment(targetCard, comment)

    if ErrorMessage != '':
      return ErrorMessage
    else:
      return 'done'

  #Comment the approved Promote under the card of the user
  def makePromDemComment(self, targetCard, comment):  #Comment has to be formated as dictionary
    targetCard.comment(f'Wer: {comment[0]}\nVon wem: {comment[1]}\nRang: [{comment[2]}]->[{comment[3]}]\nGrund: {comment[4]}\nDatum: {comment[5]}\nSteamID: {comment[6]}') ##steamID is implicit (nedded to find card)
   

  #Comment the approved positive or negative 
  def makePoNeComment(self, steamID, comment):  #Comment has to be formated as dictionary 
    targetCard = self.getCardFromSteamID(steamID)

    targetCard.comment(f'Wer: {comment[0]}\nVon wem: {comment[1]}\nGrund: {comment[2]}\n\nDatum: {comment[3]}\nSteamID: {steamID}') ##steamID is implicit (nedded to find card)
  
  




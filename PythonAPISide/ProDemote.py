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

  def getCardFromSteamID(self, steamID):
    currentBoard = self.client.get_board(config.__boardid__)
    print(currentBoard.name) ##justTest case
    # Get all the list in the board 
    all_lists = currentBoard.open_lists() 
    
    # Get all relevant Lists and Cards
    for currentList in all_lists[1:]:     #später [1:] machen um die standartdaten zu übersprüngen
      for currentCard in currentList.list_cards():
        CardData = {}

        #find corresponding card for the SteamID
        if not currentCard.name.__contains__('-'):

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
    #for label in __selectedCard__.
    targetCard.change_pos()
    targetCard.change_list()
    #return f'Name: {__selectedCard__.name}\nVom Rang: {}'


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
    targetCard = self.getCardFromSteamID(steamID)
    ErrorMessage = CardOperations.change_label_of_card(card_id=targetCard.id, oldRank=comment[2], newRank=comment[3])    ###comment will be a discturnary, where we get the oldRank and new Rank from
    #addPromoteSperre set_custom_field(self, value, custom_field)
    CardOperations.sortin_card(targetCard)
    self.makePromDemComment(targetCard, comment)

    if ErrorMessage != '':
      return ErrorMessage

  #Comment the approved Promote under the card of the user
  def makePromDemComment(self, targetCard, comment):  #Comment has to be formated as dictunary
    targetCard.comment(f'Wer: {comment[0]}\nVon wem: {comment[1]}\nRang: [{comment[2]}]->[{comment[3]}]\nGrund: {comment[4]}\nDatum: {comment[5]}\nSteamID: {steamID}') ##steamID is implicit (nedded to find card)
   

  #Comment the approved positive or negative 
  def makePoNeComment(self, steamID, comment):  #Comment has to be formated as dictunary 
    targetCard = self.getCardFromSteamID(steamID)

    targetCard.comment(f'Wer: {comment[0]}\nVon wem: {comment[1]}\nGrund: {comment[2]}\n\nDatum: {comment[3]}\nSteamID: {steamID}') ##steamID is implicit (nedded to find card)
  
  




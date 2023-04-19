from trello import TrelloClient
from trello import card, base, label
from trello.customfield import CustomField, CustomFieldText, CustomFieldCheckbox, CustomFieldNumber, CustomFieldDate, CustomFieldList
import pandas as pd
import config

class ProDemote:

  client = TrelloClient(
      api_key= config.__myApi_key__,
      api_secret= config.__myApi_secret__,
      token= config.__myToken__,
      #token_secret='your-oauth-token-secret'
  )

  #improve performance, by just sarching for the Card(SteamID) one time
  __selectedCard__ = ""


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
          
          if CardData.get('SteamID')[0] == steamID:
            __selectedCard__ = currentcard
            

  ###WORK IN PROGRESS
  #get only name and Rank for the ProDemote form
  def getNameAndRankFromSteamID(self, steamID):
    self.getCardFromSteamID(steamID)

    #for label in __selectedCard__.

    #return f'Name: {__selectedCard__.name}\nVom Rang: {}'


  #return every Data of a User
  def getDataOfUser(self, steamID):
    self.getCardFromSteamID(steamID)

    CardData = {} #where to save the Data of the fields

    for custom_fields in self.__selectedCard__.custom_fields: 
        
        # Get the custom fields Data
        for custom_fields in self.__selectedCard__.custom_fields: 
          CardData[custom_fields.name]= [custom_fields.value]

    return CardData
  
  
  ##WORK IN PROGRESS#promote or demote a user
  def proDemoteUser(self, steamID, comment, ranksystem):  #ranksystem is dicturenary with the ranks of the specific Unit
    self.getCardFromSteamID(steamID)
    
    #changelabels
    #sort
    self.makePromDemComment(steamID, comment)


  ##WORK IN PROGRESS#changeLabel(Rank)
  def changeLabelOfCard(self, newRank):
    self.__selectedCard__.


  #Comment the approved Promote under the card of the user
  def makePromDemComment(self, steamID, comment):  #Comment has to be formated as dictunary
    self.getCardFromSteamID(steamID)

    self.__selectedCard__.comment(f'Wer: {comment[0]}\nVon wem: {comment[1]}\nRang: [{self.__selectedCard__.l}]->[{comment[3]}]\nGrund: {comment[4]}\nDatum: {comment[5]}\nSteamID: {steamID}') ##steamID is implicit (nedded to find card)
  

  #Comment the approved positive or negative 
  def makePoNeComment(self, steamID, comment):  #Comment has to be formated as dictunary
    self.getCardFromSteamID(steamID)

    self.__selectedCard__.comment(f'Wer: {comment[0]}\nVon wem: {comment[1]}\nGrund: {comment[2]}\n\nDatum: {comment[3]}\nSteamID: {steamID}') ##steamID is implicit (nedded to find card)
  
  




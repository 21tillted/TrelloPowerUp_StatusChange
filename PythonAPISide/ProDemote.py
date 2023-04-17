from trello import TrelloClient
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

  #improve performanc, by just sarching one time for Card(SteamID)
  __selectedCard__ = ''

  def getCardFromSteamID(self, steamID):
    currentBoard = self.client.get_board(config.__boardid__)
    print(currentBoard.name) ##justTest case
    # Get all the list in the board 
    all_lists = currentBoard.open_lists() 
    
    # Get all relevant Lists and Cards
    for currentlist in all_lists[1:]:
      for currentcard in currentlist.list_cards():
        dict = {}
        #find corresponding card for the SteamID
        if not currentcard.name.__contains__('-'):
          
          for custom_fields in currentcard.custom_fields: 
            dict[custom_fields.name]= [custom_fields.value]
          
          list_of_key = list(dict.keys())
          list_of_value = list(dict.values())

          print(list_of_key,list_of_value)
          print(currentcard)
          __selectedCard__ = currentcard
        

  def getNameAndRankFromSteamID(self, steamID):
    self.getCardFromSteamID(steamID)
    card = self.__selectedCard__
    df = pd.DataFrame()

    for custom_fields in card.custom_fields: 
        dict[custom_fields.name]= [custom_fields.value]

    
        df1 = pd.DataFrame()
        if not card.closed:
          dict['Card Name']=[card.name]
          dict['List Name']=[list.name] 
          # Get the custom fields
          for custom_fields in card.custom_fields: 
            dict[custom_fields.name]= [custom_fields.value]

          # Create a data frame with card ,list , custom field in card
          df1 = pd.DataFrame(dict) 
          # Merge the dataframe in order to add all card's custom fields
          df =pd.concat([df, df1], ignore_index=True, sort=False) 


    return 'Name: {name}\nVom Rang: {rank}'

  #Forlater
  #Add comment
  #card.comment("Dui faucibus in ornare quam viverra orci sagittis.")
  #changeLabel(Rank)
  def changeRankOfCard(self, newRank):
    labelsOfCard = self.card.labels




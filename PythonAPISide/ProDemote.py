from trello import TrelloClient
from trello.customfield import CustomField, CustomFieldText, CustomFieldCheckbox, CustomFieldNumber, CustomFieldDate, CustomFieldList
import pandas as pd
import config
from enum import Enum

steamID = "STEAM_0:0:121430886"



client = TrelloClient(
    api_key= config.__myApi_key__,
    api_secret= config.__myApi_secret__,
    token= config.__myToken__,
    #token_secret='your-oauth-token-secret'
)

currentBoard = client.get_board(config.__boardid__)

# Get all the list in the board 
all_lists = currentBoard.open_lists() 
df = pd.DataFrame()
# Get list name and cards in it (Card name)
for list in all_lists[1:]:
 for card in list.list_cards():
  
  if not card.name.__contains__('-'):
    print(card)
  # dict = {}
  # df1 = pd.DataFrame()
  # if not card.closed:
  #   dict['Card Name']=[card.name]
  #   dict['List Name']=[list.name] 
  #   # Get the custom fields
  #   for custom_fields in card.custom_fields: 
  #     dict[custom_fields.name]= [custom_fields.value]

  #   # Create a data frame with card ,list , custom field in card
  #   df1 = pd.DataFrame(dict) 
  #   # Merge the dataframe in order to add all card's custom fields
  #   df =pd.concat([df, df1], ignore_index=True, sort=False) 


#Forlater
#Add comment
#card.comment("Dui faucibus in ornare quam viverra orci sagittis.")
#changeLabel(Rank)
labelsOfCard = card.labels

print(currentBoard.name)



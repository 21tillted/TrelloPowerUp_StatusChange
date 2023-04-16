from trello import TrelloClient
from trello.customfield import CustomField, CustomFieldText, CustomFieldCheckbox, CustomFieldNumber, CustomFieldDate, CustomFieldList
import pandas as pd

steamID = "STEAM_0:0:121430886"

myApi_key='f9274211f281c4ceba5ce109481d25c5'
myApi_secret='4b84310cca4ec4fb2d8138c65811dcfc04fdaaa3d3c44b6187820dc37fc38c5f'
myToken='ATTAedd540d14edadf2f5eac6bb4570dec3fdb49e968f7511c152bf7f816838e0b62C0364953'
token_secret=''

client = TrelloClient(
    api_key= myApi_key,
    api_secret= myApi_secret,
    token= myToken,
    #token_secret='your-oauth-token-secret'
)

all_boards = client.list_boards()
last_board = all_boards[-1]

currentBoard = client.get_board('8hSBNmno')
#cards = currentBoard.get_cards('all','all')

# Get all the list in the board 
all_lists = currentBoard.open_lists() 
df = pd.DataFrame()
# Get list name and cards in it (Card name) 
for list in all_lists: 
 for card in list.list_cards(): 
   dict = {} 
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


#Forlater
#Add comment
#card.comment("Dui faucibus in ornare quam viverra orci sagittis.")
#changeLabel(Rank)
labelsOfCard = card.labels

print(currentBoard.name)



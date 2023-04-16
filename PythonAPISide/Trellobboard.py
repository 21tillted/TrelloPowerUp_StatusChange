from trello import TrelloClient
from trello.customfield import CustomField, CustomFieldText, CustomFieldCheckbox, CustomFieldNumber, CustomFieldDate, CustomFieldList
import json

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
cards = currentBoard.get_cards('all','all')

for card in cards:
    comment = json.dumps(card.comments) 
    card.customFields.
    if comment.get('SteamID') == steamID:
        print(card.name)
        print("true")

print(currentBoard.name)



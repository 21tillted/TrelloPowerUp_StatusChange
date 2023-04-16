from trello import TrelloClient
from 0Auth import create_oauth_token

myapi_key='f9274211f281c4ceba5ce109481d25c5'
myapi_secret='4b84310cca4ec4fb2d8138c65811dcfc04fdaaa3d3c44b6187820dc37fc38c5f'

create_oauth_token(myapi_key, myapi_secret)

client = TrelloClient(
    api_key= myapi_key,
    api_secret= myapi_secret,
    token='your-oauth-token-key',
    token_secret='your-oauth-token-secret'
)

all_boards = client.list_boards()
last_board = all_boards[-1]


print(last_board.name)



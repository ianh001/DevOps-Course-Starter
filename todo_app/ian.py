import requests
import os
import dotenv
#from todo_app.data.item import Item

dotenv.load_dotenv()

key = os.getenv("TRELLO_KEY")
token = os.getenv("TRELLO_TOKEN")
board_id = os.getenv("TRELLO_BOARD_ID")




response = requests.get(f"https://api.trello.com/1/boards//{board_id}/lists/?key={key}&token={token}&lists=all")
#response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={key}&token={token}&cards=open")
        
response_json = response.json()

list_of_list = []

for board_list in response_json:
    itemid = {
        "list_name": board_list["name"],
        "list_id": board_list["id"]
    }

    list_of_list.append(itemid)

print(list_of_list)
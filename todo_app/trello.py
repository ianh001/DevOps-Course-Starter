import requests
import os
import dotenv
#from todo_app.data.item import Item

dotenv.load_dotenv()

key = os.getenv("TRELLO_KEY")
token = os.getenv("TRELLO_TOKEN")
board_id = os.getenv("TRELLO_BOARD_ID")

def get_item(item_id):
    items = get_items()
    for item in items:
        if item['id'] == item_id:
            return item
    return None

def get_items_all():

    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={key}&token={token}&cards=open")
        
    response_json = response.json()

    return response_json

def get_items():

    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={key}&token={token}&cards=all")
 
    response_json = response.json()

    list_of_cards = []

    for trello_list in response_json:
        list_name = trello_list["name"]
        cards = trello_list["cards"]
        
        for card in cards:
            item = {
                "title": card["name"],
                "id": card["id"],
                "status" : list_name            
            }
            list_of_cards.append(item)
    return list_of_cards 

def get_list_ids():
    response = requests.get(f"https://api.trello.com/1/boards//{board_id}/lists/?key={key}&token={token}&lists=all")
    response_json = response.json()
    
    list_of_lists = []

    for board_list in response_json:
        itemid = {
            "list_name": board_list["name"],
            "list_id": board_list["id"]
        }

        list_of_lists.append(itemid)

    return list_of_lists             
                            

def add_item(title):
     
   for trello_list in get_list_ids():
        if trello_list["list_name"] == "To Do":
            list_id = trello_list["list_id"]     
   item = requests.post(f"https://api.trello.com/1/cards?key={key}&token={token}&name={title}&desc=test discription&idList={list_id}")          
   return item

def complete_item(item_id):
    lists = get_list_ids()
    done_list_id = next((list_item['list_id'] for list_item in lists if list_item['list_name'] == 'Done'), None)
    
    if done_list_id:
        response = requests.put(f"https://api.trello.com/1/cards/{item_id}?key={key}&token={token}",
                               params={"idList": done_list_id})
        return response.json()
    else:
        return None



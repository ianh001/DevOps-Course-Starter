import requests
import os
import dotenv

dotenv.load_dotenv()

key = os.getenv('TRELLO_KEY')
token = os.getenv('TRELLO_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')

def get_items():
  reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"

  query_params = {
      "key": key,
      "token": token,
      "cards": "open",
      "card_fields": "id,name"
  }

  response = requests.get(reqUrl, params=query_params)

  response_json = response.json()

 # cards = []
 # for trello_list in response_json:
 #   for card in trello_list['cards']:
 #     cards.append(card)

  #print(cards)
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
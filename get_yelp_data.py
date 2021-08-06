import os
import json

API_TOKEN = os.getenv('API_TOKEN')
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
}

def convert_json_to_dict(json_file:str) -> dict:
    with open(json_file, encoding='utf-8') as json_file:
        return json.load(json_file)

def get_yelp_data(restaurant:dict) -> dict:
    pass

def update_restaurant_json_file(yelp_data:dict) -> None:
    pass

def update_restaurants_with_yelp_data(restaurants:list) -> None:
    pass

def is_similar(restaurant_name:dict) -> bool:
    pass

if __name__ =='__main__':
    restaurants_dict = convert_json_to_dict("restaurant_data.json")
    update_restaurants_with_yelp_data()
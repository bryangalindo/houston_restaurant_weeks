import os
import json

import requests


API_KEY = os.getenv('API_KEY')
headers = {
    "Authorization": f"Bearer {API_KEY}",
}

yelp_api_endpoint = 'https://api.yelp.com/v3/businesses/search?term={}&latitude={}&longitude={}'

def convert_json_to_dict(json_file:str) -> dict:
    with open(json_file, encoding='utf-8') as json_file:
        return json.load(json_file)
    
def filter_yelp_response(response:dict) -> dict:
    if len(response["businesses"]) != 0:
        restaurant_node = response["businesses"][0]
        return {
            "yelp_id": restaurant_node["id"],
            "yelp_name": restaurant_node["name"], 
            "review_count": restaurant_node["review_count"], 
            "rating": restaurant_node["rating"], 
            "caategories": restaurant_node["categories"], 
            "phone": restaurant_node["phone"],
            "yelp_url": restaurant_node["url"].split('?')[0],
        }

def get_yelp_data(restaurant:dict) -> dict:
    response = requests.get(
        url=yelp_api_endpoint.format(
            restaurant['name'], 
            restaurant['coordinates']['latitude'], 
            restaurant['coordinates']['longitude'],
            ),
        headers=headers)
    return filter_yelp_response(response.json())

def update_restaurant_json_file(yelp_data:dict) -> None:
    pass

def update_restaurants_with_yelp_data(restaurants:list) -> None:
    pass

def is_similar(restaurant_name:dict) -> bool:
    pass

if __name__ =='__main__':
    restaurants_dict = convert_json_to_dict("restaurant_data.json")
    restaurant = {
            "name": "Acadian Coast",
            "hrw_url": "https://houstonrestaurantweeks.com/restaurants/acadian-coast/",
            "coordinates": {
                "latitude": "29.7564351",
                "longitude": "-95.3401952"
            }
        }
    print(get_yelp_data(restaurant))

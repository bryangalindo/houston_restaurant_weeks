import json
import logging
import os

import requests


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

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
        filtered_yelp_response = {
            "yelp_id": restaurant_node["id"],
            "yelp_name": restaurant_node["name"], 
            "review_count": restaurant_node["review_count"], 
            "rating": restaurant_node["rating"], 
            "categories": restaurant_node["categories"], 
            "phone": restaurant_node["phone"],
            "yelp_url": restaurant_node["url"].split('?')[0],
        }
        logging.info(f'Filtered Yelp response. Result: {filter_yelp_response}')
        return filtered_yelp_response
    else:
        logging.warning(f'Yelp Search API did not return businesses')

def get_yelp_data(restaurant:dict) -> dict:
    url = yelp_api_endpoint.format(
        restaurant['name'], 
        restaurant['coordinates']['latitude'], 
        restaurant['coordinates']['longitude']
        )
    logging.info(f'Gathering Yelp data for {url}')
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        logging.info('Success call to Yelp API!')
        filtered_dict = filter_yelp_response(response.json())
        return filtered_dict
    else:
        logging.warning(f'Unsuccessful call to Yelp API. Status code: {response.status_code}')

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

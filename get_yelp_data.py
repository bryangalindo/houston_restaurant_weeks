from difflib import SequenceMatcher
import json
import logging
import os
import sys

import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('error_logs.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

API_KEY = os.getenv('API_KEY')
headers = {"Authorization": f"Bearer {API_KEY}"}

yelp_api_endpoint = 'https://api.yelp.com/v3/businesses/search?term={}&latitude={}&longitude={}'


def is_similar(a:str, b:str) -> bool:
    ratio = SequenceMatcher(None, a, b).ratio()
    if ratio > .5:
        return True
    else:
        logging.WARNING(f'HRW name {a} is not similar to Yelp\'s first search result {b}.')
        return False

def convert_json_to_dict(json_file:str) -> dict:
    with open(json_file, encoding='utf-8') as json_file:
        return json.load(json_file)
    
def filter_yelp_response(restaurant_name:str, response:dict) -> dict:
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
        logger.info(f'Filtered Yelp response. Result: {filtered_yelp_response}.')
        return filtered_yelp_response
    else:
        warning = f'Yelp Search API did not return any businesses for {restaurant_name}.'
        logger.warning(warning)

def get_yelp_data(restaurant:dict) -> dict:
    url = yelp_api_endpoint.format(
        restaurant['name'], 
        restaurant['coordinates']['latitude'], 
        restaurant['coordinates']['longitude']
        )
    logger.info(f'Gathering Yelp data for {url}')
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        logger.info('Success call to Yelp API!')
        filtered_dict = filter_yelp_response(restaurant['name'], response.json())
        return filtered_dict
    else:
        logger.warning(f'Unsuccessful call to Yelp API. Status code: {response.status_code}. {response.reason}.')

def update_restaurant_json_file(yelp_data:dict) -> None:
    pass

def update_all_restaurants_with_yelp_data(restaurants:list) -> None:
    pass

def is_similar(restaurant_name:dict) -> bool:
    pass

if __name__ =='__main__':
    restaurants_dict = convert_json_to_dict("restaurant_data.json")
    for restaurant in restaurants_dict['restaurants']:
        get_yelp_data(restaurant)
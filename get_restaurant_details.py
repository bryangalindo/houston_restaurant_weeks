import json
import logging 
import os
import time

import requests
from bs4 import BeautifulSoup


API_TOKEN = os.getenv('API_TOKEN')
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
        "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Authorization": f"Bearer {API_TOKEN}",
    }

def get_restaurant_url_list(text_file: str) -> list:
    with open(text_file, 'r', encoding='utf-8') as f:
        return [url.strip() for url in f]
        
def get_restaurant_data(url: str) -> dict:
    logging.info(f'Scraping {url}')
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logging.info('Successful request')
        html = BeautifulSoup(response.content, 'html.parser')
        name = html.find('h1').text if html.find('h1') else ''
        latitude = html.find("input", {"id": "latitude"}).get('value', {})
        longitude = html.find("input", {"id": "longitude"}).get('value', {})
        return {
            'name': name,
            'hrw_url': url,
            'coordinates': {
                'latitude': latitude,
                'longitude': longitude,
            }
        }
    else:
        logging.warning(f'Request was not successful. Status code: {response.status_code}')

def generate_restaurant_data_list(urls: list) -> list:
    restaurant_data_list = []
    logging.info(f'Beginning to scrape {len(urls)} urls')
    for url in urls:
        restaurant_data = get_restaurant_data(url)
        restaurant_data_list.append(restaurant_data)
        time.sleep(1)
    return restaurant_data_list

def generate_json_file(coordinates: list, output_file: str) -> None:
    restaurants_dict = {
        'restaurants': coordinates
    }
    with open(output_file, 'w', encoding='utf8') as outfile:
        logging.info('Writing restaurant data to json file')
        json.dump(restaurants_dict, outfile, ensure_ascii=False)
                
if __name__ == '__main__':
    urls = get_restaurant_url_list('restaurant_urls.txt')
    restaurant_data = generate_restaurant_data_list(urls)
    generate_json_file(restaurant_data, 'restaurant_data.json')
    
    
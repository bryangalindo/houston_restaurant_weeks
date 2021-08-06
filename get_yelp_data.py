import os


API_TOKEN = os.getenv('API_TOKEN')
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
}

def get_restaurant_data_dict(json_file:str) -> dict:
    pass

def get_yelp_data(restaurant:dict) -> dict:
    pass

def update_restaurant_json_file(yelp_data:dict) -> None:
    pass

def update_restaurants_with_yelp_data(restaurants:list) -> None:
    pass

def is_similar(restaurant_name:dict) -> bool:
    pass

if __name__ =='__main__':
    restaurants_dict = get_restaurant_data_dict("restaurant_data.json")
    update_restaurants_with_yelp_data()
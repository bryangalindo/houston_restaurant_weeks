import requests
from bs4 import BeautifulSoup
from pprint import pprint


# url = 'https://houstonrestaurantweeks.com/restaurants/eighteen36/'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
#         "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
#     }
# response = requests.get(url, headers=headers)
# html = BeautifulSoup(response.content, "html.parser")

# with open('restaurant.html', 'w') as f:
#     f.write(str(html))

with open('restaurant.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    restaurant_info_table = soup.find('table', {'class': 'info'})
    restaurant_info_rows = restaurant_info_table.find_all('td')
    restaurant_info = [row.text for row in restaurant_info_rows]
    print(restaurant_info)

    menu_options_table = soup.find('div', {'class': 'tab_container'})
    dinner_menu_element = menu_options_table.find('div', {'id': 'dinnerMenu'})
    lunch_menu_element = menu_options_table.find('div', {'id': 'lunchMenu'})
    brunch_menu_element = menu_options_table.find('div', {'id': 'brunchMenu'})
    print(dinner_menu_element.text)
    print(lunch_menu_element.text)
    print(brunch_menu_element.text)


    
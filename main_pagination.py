import requests #HTTP requests
import json 
from config import cookies, headers
import os # interacting with the file system
import math
def get_data():
    """
Initializes parameters for the HTTP request.
Checks if the data directory exists, creates it if not.
Creates a requests.Session() to maintain a persistent HTTP session.
Makes an initial GET request to fetch the total number of products and calculates the number of pages.
Iterates over each page, fetching product IDs, descriptions, and prices.
Saves this data into three separate JSON files: 1_products_ids.json, 2_products_descriptions.json, and 3_products_prices.json.
    """
    
    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
            'WyJza2lka2EiLCIiLCJkYSJd',
        ],
        'doTranslit': 'true',
    }

    if not os.path.exists('data'):
        os.mkdir('data')
    
    s = requests.Session()
    response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    # print(response)
    total_items = response.get('body').get('total')

    if total_items is None:
        return '[!] No items or Error'
    pages_count = math.ceil(total_items / 24)

    print(f'[INFO] Total positions: {total_items} | Total pages: {pages_count}')

    products_ids = {}
    products_description = {}
    products_prices = {}

    for i in range(pages_count):
        offset = f'{i*24}' #смещение
        params = {
            'categoryId': '118',
            'offset': offset,
            'limit': '24',
            'filterParams': [
                'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
                'WyJza2lka2EiLCIiLCJkYSJd',
            ],
            'doTranslit': 'true',
    }
        
        response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

        products_ids_list = response.get('body').get('products')
        products_ids[i] = products_ids_list
        json_data = {
            'productIds': products_ids_list,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }

        response = s.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
        products_description[i] = response

        products_ids_str = ','.join(products_ids_list)
        params = {
            'productIds': products_ids_str,
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
            }

        response = s.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

        material_prices = response.get('body').get('materialPrices')
        for item in material_prices:
            item_id = item.get('price').get('productId')
            item_base_price = item.get('price').get('basePrice')
            item_sale_price = item.get('price').get('salePrice')
            item_bonus = item.get('bonusRubles').get('total')

            products_prices[item_id] = {
                'item_basePrice' : item_base_price,
                'item_salePrice' : item_sale_price,
                'item_bonus' : item_bonus
            }

        print(f'[+] Finished {i + 1} of the {pages_count} pages')

    with open('data/1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    
    with open('data/2_products_descriptions.json', 'w', encoding='utf-8') as file:
        json.dump(products_description, file, indent=4, ensure_ascii=False)

    with open('data/3_products_prices.json', 'w') as file:
        json.dump(products_prices, file, indent=4, ensure_ascii=False)


def get_result():
    """
Reads the product descriptions and prices from the JSON files.
Merges the price information into the product descriptions.
Saves the merged data into 4_result.json.
    """
    with open('data/2_products_descriptions.json','r', encoding='utf-8') as file:
        products_data = json.load(file)
    
    with open('data/3_products_prices.json') as file:
        products_prices = json.load(file)
    
    for items in products_data.values():
        products = items.get('body').get('products')
        for item in products:
            product_id = item.get('productId')

            if product_id in products_prices:
                prices = products_prices[product_id]
            
            item['item_basePrice'] = prices.get('item_basePrice')
            item['item_salePrice'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')
            item['item_link'] = f'https://www.mvideo.ru/products/{item.get("nameTranslit")}-{product_id}'
    
    with open('data/4_result.json', 'w', encoding='utf-8') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()




if __name__ == '__main__':
    main()
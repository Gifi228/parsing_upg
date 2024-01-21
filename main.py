import requests
from bs4 import BeautifulSoup
from time import time
from baseparser import *
from product_page import *
from database import *


class UpgParser(BaseParser, Additional):
    def __init__(self):
        super(UpgParser, self).__init__()

    def get_data(self):
        soup = self.get_soup(self.get_html())
        filter_item = soup.find('div', class_='fi-tablet-left')
        categories = filter_item.find_all('li', {'class': 'dropdown-submenu'})
        for category in categories:
            category_title = category.find('a').get_text(strip=True)
            category_link = category.find('a').get('href')
            print(category_title)
            print(category_link)

            insert_category(category_title, category_link)

            self.get_products_page(category_title, category_link)

    def get_products_page(self, category_title, category_link):
        category_id = get_category_id(category_title)
        soup = self.get_soup(self.get_html(category_link))
        product_grid = soup.find('div', class_='product-grid')
        products = product_grid.find_all('div', class_='item-product')
        for product in products[:3]:
            product_title = product.find('a', class_='item-link').get_text(strip=True)
            product_link = product.find('a', class_='item-link').get('href')
            print(product_title)
            print(product_link)
            try:
                product_price = product.find('span', class_='item-price').get_text(strip=True)
                product_price = int(product_price.replace(' ', '').replace('сум', ''))
            except:
                product_price = 0

            product_image = self.HOST + product.find('img').get('src')
            print(product_image)

            desc = self.get_product_description(link=product_link)
            insert_product_data(category_id, product_title, product_link, product_price, product_image, desc)

            product_id = get_product_id(product_title)

            characteristics = self.get_product_characteristics(link=product_link)
            insert_characteristic(product_id, characteristics)


def start_parsing():
    start = time()
    parser = UpgParser()
    parser.get_data()
    finish = time()
    print(f"Парсер отработал за {finish - start} секунд")


start_parsing()

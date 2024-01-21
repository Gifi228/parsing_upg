from bs4 import BeautifulSoup
import requests


class BaseParser:
    def __init__(self):
        self.URL = 'https://upg.uz/ru'
        self.HOST = 'https://upg.uz'

    def get_html(self, url=None):
        if url:
            html = requests.get(url).text
        else:
            html = requests.get(self.URL).text
        return html

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

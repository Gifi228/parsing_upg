# https://upg.uz/ru/products/sborka-12-14700kf-4080-32gb-500gb
import requests
from bs4 import BeautifulSoup


class Additional:
    def get_product_description(self, link):
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        try:
            desc = soup.find('div', {'id': 'tab-1'}).get_text(strip=True)
        except:
            desc = 'Нет информации !'
        finally:
            return desc

    def get_product_characteristics(self, link):
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        try:
            config = soup.find('div', {'id': 'tab-2'})
            config_item = config.find_all('tr')
            characteristics = {}
            for item in config_item:
                title = item.find('th').get_text(strip=True)
                info = item.find_next("td").get_text(strip=True)
                print(title)
                print(info)
                characteristics.update({title: info})
            return characteristics
        except:
            characteristics = {'info': 'Нет информации !'}
        finally:
            return characteristics

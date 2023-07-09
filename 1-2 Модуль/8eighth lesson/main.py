#bs4 - библиотека для парсинга страниц
import requests
from BeautifulSoup4 import BeautifulSoup # Красивый суп

url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='

response = requests.get(url).content #Каша, в котрой ничего нельзя вытащить отдельно

xml = BeautifulSoup(response, 'html.parser')#Распарсили кашу и получили красивый суп,
                                            # в котором есть отдельный элементы


res = xml.find('valute', {'id': 'R01235'})

# print(response)
# print(xml)
print(res)
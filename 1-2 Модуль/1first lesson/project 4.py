import requests
import random
from bs4 import BeautifulSoup

def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    print(fact.text)
    print(fact.a.attrs['href'])

get_fact()

# a = 10
# while a>0:
#     print(a)
#     a-=1

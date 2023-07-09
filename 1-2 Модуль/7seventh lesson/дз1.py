import requests

list = []

url = 'https://swapi.dev/api/'

response = requests.get(url).json()

starships_api = response.get('starships')

def check_starships(url):
    for i in range(10, 14):
        response = requests.get(url + str(i)).json()
        list.append(response['max_atmosphering_speed'])

list.append(check_starships(starships_api))
list = list[:-1]
max_speed = max(list)

print('Наибольшая максимальная скорость - ' + max_speed)
import requests

url = 'https://swapi.dev/api/'

response = requests.get(url).json()

starships_api = response.get('starships')

def check_starships(url):
    for i in range(10, 14):
        response = requests.get(url + str(i)).json()
        print(response['name'], response['max_atmosphering_speed'])


check_starships(starships_api)
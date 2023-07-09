import requests

url = 'https://swapi.dev/api/'

response = requests.get(url).json()

# people_api = requests.get(response['people']).json()
people_api = response['people']

# print(people_api['results'][0]['name'])


def check_people(url):
    for i in range(1, 6):
        # print(url + str(i))
        response = requests.get(url + str(i)).json()
        print(response['name'], response['height'])

print(people_api)

check_people(people_api)
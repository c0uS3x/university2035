import requests
import vk_api

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

token = 'vk1.a.aDm2H2hSIzP8CxDV6rV3ipuWTI52t5ImIHvKXNbkNgVgsw6XmWkUZYkUtMZPfsIwkUaHnEptQ-wMXo_Er6X6FpP06N8Ad5Xij3K3BZbgSyDyfKDwIACp__VmBTvpyTzY0QUOVbKizEbe1AjBll7BgVHjDmrK_7Aky9e3bqGjqt3iVS6ELYtUT83SclnPx_-okc2HktcCzMXcYZZQzsRScQ'

vk_sessinon = vk_api.VkApi(token=token)

vk = vk_sessinon.get_api()


while True:
    messages = vk.messages.getConversations(count=20, filter='unanswered')
    if messages['count'] >= 1:
        messages_text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['random_id']
        if messages_text.lower() == 'корабли':
            vk.messages.send(user_id=user_id, random_id=message_id, message=f'Наибольшая максимальная скорость корабля - {max_speed}')
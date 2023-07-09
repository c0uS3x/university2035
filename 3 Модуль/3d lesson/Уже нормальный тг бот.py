import vk_api
from vk_api.longpoll import VkLongPoll

token = 'vk1.a.aDm2H2hSIzP8CxDV6rV3ipuWTI52t5ImIHvKXNbkNgVgsw6XmWkUZYkUtMZPfsIwkUaHnEptQ-wMXo_Er6X6FpP06N8Ad5Xij3K3BZbgSyDyfKDwIACp__VmBTvpyTzY0QUOVbKizEbe1AjBll7BgVHjDmrK_7Aky9e3bqGjqt3iVS6ELYtUT83SclnPx_-okc2HktcCzMXcYZZQzsRScQ'

vk_sessinon = vk_api.VkApi(token=token)

vk = vk_sessinon.get_api()

longpoll = VkLongPoll(vk_sessinon)

for event in longpoll.listen():
    if event.type == 4 and event.to_me:
        text = event.text
        user_id = event.user_id
        message_id = event.message_id
        if text.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=message_id, message='Привет сладенький')
        else:
            vk.messages.send(user_id=user_id, random_id=message_id, message='z yt gjybvf. nt,z')
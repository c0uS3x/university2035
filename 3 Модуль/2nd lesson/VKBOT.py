import vk_api


token = 'vk1.a.aDm2H2hSIzP8CxDV6rV3ipuWTI52t5ImIHvKXNbkNgVgsw6XmWkUZYkUtMZPfsIwkUaHnEptQ-wMXo_Er6X6FpP06N8Ad5Xij3K3BZbgSyDyfKDwIACp__VmBTvpyTzY0QUOVbKizEbe1AjBll7BgVHjDmrK_7Aky9e3bqGjqt3iVS6ELYtUT83SclnPx_-okc2HktcCzMXcYZZQzsRScQ'

vk_sessinon = vk_api.VkApi(token=token)

vk = vk_sessinon.get_api()


while True:
    messages = vk.messages.getConversations(count=20, filter='unanswered')
    if messages['count'] >= 1:
        messages_text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['random_id']
        if messages_text.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=message_id, message='hi')


# print(messages['items'][0]['last_message']['text'])
import telebot
import random


token = '6182900628:AAGyyf_Z7kVHFwxd6QIXEN9b3FJhBBYaeH0'    #API-токен

bot = telebot.TeleBot(token)    #Идентифицировали бота из ТГ


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = 'Привет!Я умею сочинять  стихи и отправлять милых котиков!'
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = 'Йоу репчик жесть'
    bot.send_message(message.chat.id, poem_text)


@bot.message_handler(commands=['cat'])
def send_cats(message):
    # cat_img =  open('img/4.jpg', 'rb')
    # bot.send_photo(message.chat.id, cat_img)

    cat_number = str(random.randint(1, 41))
    cat_img = open(f'img/{cat_number}.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)


bot.polling()

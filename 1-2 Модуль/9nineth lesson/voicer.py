import pyaudio
import speech_recognition as sr
import pyttsx3
import random
import webbrowser


rec = sr.Recognizer()               #Распознаватель

voice = pyttsx3.init()
voice.say('Привет! Я голосовой помощник!')
voice.runAndWait()

list_hi = ['привет', "хай", "ёу"]

while True:
    with sr.Microphone(device_index=1) as source:
        # rec.adjust_for_ambient_noise(source, duration=1)  #Додж шумов
        print('Скажите что-нибудь...')
        audio = rec.listen(source)
    text = rec.recognize_google(audio, language='ru_RU')
    # voice.say(text + 'буээээээ')
    # voice.runAndWait()

    if 'привет' in text.lower():
        voice.say(random.choice(list_hi))
        voice.runAndWait()
    elif 'как дела' in text.lower():
        voice.say('пока не родила!')
        voice.runAndWait()
    elif 'youtube' in text.lower():
        webbrowser.open_new('https://www.youtube.com/?hl=ru&gl=RU')
        voice.say('ютуб запущен!')
        voice.runAndWait()

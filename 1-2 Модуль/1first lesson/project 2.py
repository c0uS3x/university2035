'''films = {
    'Начало': 'Леонардо Ди Каприо',
    'Пираты Карибского моря': 'Джонни Депп',
    'Миссия невыполнима': 'Том Круз'
}

actor = 'Том Круз'
film = input('Какой фильм будем смотреть')

if film in films:
    actor_2 = films.get(film)
    if actor == actor_2:
        print('Я буду смотреть этот фильм')
    else:
        print('Я не хочу смотреть это кино')
else:
    print('Такого фильма в нашей базе нет')'''
        


'''raiting = int(input('Какой рейтинг у фильма? '))
if actor == actor_2 and raiting > 7:
    print('Я буду смотреть этот фильм')
elif actor == actor_2 or raiting > 7:
    print('Должен быть неплохой фильм')
else:
    print('Я не хочу смотреть это кино')'''

def soup() :
    a = input("Введите овощ ")
    b = input("Введите мясо ")
    print(f'Ваш суп с {a} и {b} готов! Приятного аппетита!')

soup()

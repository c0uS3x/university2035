films = {
    'Начало': 'Леонардо Ди Каприо',
    'Пираты Карибского моря': 'Джонни Депп',
    'Миссия невыполнима': 'Том Круз',
    'Фильм 1': 'Актер 1'
}

reitings = {
    'Начало': '5',
    'Пираты Карибского моря':'7',
    'Миссия невыполнима':10,
    'Фильм 1':'3'
}


actor = 'Том Круз'
film = input('Какой фильм будем смотреть? ')
reiting = input('Рейтинг?')

if film in films and film in reiting:
    actor_2 = films.get(film)
    reitings.get(reiting)
    if actor == actor_2 and reiting > 7:
        print('Я буду смотреть этот фильм')
    else:
        print('Я не хочу смотреть это кино')
else:
    print('Такого фильма в нашей базе нет')

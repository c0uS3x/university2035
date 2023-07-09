# словари

# english_dict = {
#     'яблоко': 'apple',
#     'молоко': 'milk',
#     'кот': 'cat'
# }
#
# word = input('Введите слово на русском языке: ')
# if word in english_dict:
#     print(word, 'на английском языке будет:', english_dict[word])
# else:
#     print('я не знаю такое слово')

films_dict = {
    'Начало': 'Леонардо Ди Каприо',
    'Драйв': 'Райна Гослинг',
    'Пираты Карибского моря': 'Джонни Депп'
}

favorite_actor = 'Джонни Депп'

film = input('Какой фильм хотите посмотреть?: ')

if film in films_dict:
    if favorite_actor == films_dict[film]:
        print('Фильм бомба!!!')
    else:
        print('Фильм отстой!!')
else:
    print('Я такого фильма не знаю')
# temperature = []
# for i in range(7):
#     temp = int(input('Введите температуру сегодня: '))
#     temperature.append(temp)
# print('Средняя температура равна', sum(temperature)/len(temperature))

# = - присвоение
# == - сравнекие

# favorite_actor = 'Райан Гослинг'
#
# rating = int(input('Какой рейтинг у фильма?'))
# actor = input('Кто играет главную роль в этом фильме? ')
#
# if actor == favorite_actor and raiting > 7 :
#     print('Этот фильм точно стоит смотреть')
# elif actor == favorite_actor or raiting > 7 :
#     print('Должен быть неплохим')
# else:
#     print('я бы не стал тратить время')

# age = float(input('Введите ваш возраст: '))
#
# if age >= 18:
#     print('вам можно')
# elif age >= 16 and age < 18:
#     print('ты еще не дорос')
# else:
#     print('ну ты ваще лох')

# num = int(input('Введите число: '))
# if num % 2 == 0
#     print('Число четное')
# else:
#     print('Число нечетное')

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# if a > b:
#     print(a)
# else:
#     print(b)

# import random
#
# comp = random.randint(1, 11)
# flag = False
#
# while flag == False:
#     user = int(input('попробуйте угадать цифру от 1 до 10'))
#     if comp == user:
#         print("Ты угадал!!")
#         flag = True
#     elif comp - user == 1 or user - comp == 1:
#         print('Ты был близок!')
#     else:
#         print('в следующий раз получится')

import random

comp = random.randint(1, 11)
flag = False

while True:
    user = int(input('попробуйте угадать цифру от 1 до 10'))
    if comp == user:
        print("Ты угадал!!")
        break
    elif comp - user == 1 or user - comp == 1:
        print('Ты был близок!')
    else:
        print('в следующий раз получится!!!!!')

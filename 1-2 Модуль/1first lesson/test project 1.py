'''print("Hello world")
number = 100
print(number)

name = input("Введите имя: ")
print("Привет, ", name)

marks = [5,5,5,5,4,5,3,5,4]
summa = sum(marks)
#print(summa)
lenght = len(marks) #поиск кол-ва элементов
#print(lenght)
avg = sum(marks)/len(marks) #нахождение среднего значения
maximum = max(marks) #функция позволяет найти максимальное значение
minimum = min(marks) #функция позволяет найти минимальное значение
count_5 = marks.count(5) # функция находит кол-во определенного значения
print("Средняя оценка - ", str(avg))
print(f'Наивысшая оценка - {maximum}')
print("Наименьшая оценка - " + str(minimum))
print("Количество пятерок - " + str(count_5))

#посмотреть функции

import random

facts = ['Мне было лень писать факты',
         'тут должен был быть крутой факт под номером 1',
         'fact2',
         'fact 3']
print(random.choice(facts))

print(random.randint(1,10))'''

for i in range(1,10,2):
    print(i)



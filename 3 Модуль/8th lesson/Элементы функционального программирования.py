goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1400
    },
    {
        'name': 'Samsung Galaxy A23',
        'brand': 'Samsung',
        'price': 700
    },
    {
        'name': 'Xiaomi m18 lite',
        'brand': 'Xaomi',
        'price': 300
    }
]

#
# def item_price(item):
#     return item['price']


# print(sorted(goods, key=lambda item: item['price']))
#
# apple_list = filter(lambda item: item['brand'] == 'Apple', goods)
# print(list(apple_list))

numbers = ['алексей']
number_map = map(lambda item: item.capitalize() , numbers)

print(list(number_map))
for index, item in enumerate (goods):
    print(index, item)

names = ['Иван', 'Вася', 'Петр', 'Олег']
surnames = ['Иванов', 'Петров', 'Олегов']

for name, surname in zip(names, surnames):
    print(name, surname)
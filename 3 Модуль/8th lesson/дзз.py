# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#         def __repr__(self):
#             return self.brand
#
#
# items_list = {
#     Item(1000, 'Apple'),
#     Item(1200, 'Apple'),
#     Item(900, 'Samsung'),
#     Item(700, 'Samsung'),
#     Item(660, 'Xiaomi')
# }
#
# result = filter(lambda item: item.brand == 'Apple', items_list)
# print(list(result))

names_list = ['данил', 'артём', 'никита', 'влад']

# result = [x.title() for x in names_list]
result = map(lambda item: item.title(), names_list)
print(list(result))
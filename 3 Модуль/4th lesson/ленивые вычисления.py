
# my_iter = [x for x in range(1, 100_000_000)] # Строгие вычисления
#
# print(my_iter)

# my_iter = (x for x in range(1, 100_000_000))
#
# for elem in my_iter:
#     print(elem)


# my_iter = []
# for x in range(1,100_000):
#     my_iter.append(x)

# def f(a):
#     print('start')
#     return a
#     print('end')

# a = []
# for i in range(10):
#     a.append(i)
#
# print(a)

# def my_lazy_gen():
#     for x in range(10):
#         print('до', x)
#         yield x
#         print('после', x)
#
# for i in my_lazy_gen():
#     print(i)




# file = open('file.txt', 'w')
# file.write('Hello!!?????!')

# lst = []
# for i in range(10000):
#     lst.append(open('file.txt', 'w'))

# lst = []
# for i in range(10000):
#     f = open('file.txt', 'w')
#     f.write([12, 15])
#     lst.append(f)
#     f.close()


with open('file.txt', 'w') as f:
    f.write('111')
    print(f.closed)
print(f.closed)

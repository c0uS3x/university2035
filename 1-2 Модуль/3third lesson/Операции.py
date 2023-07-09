# w - write
# r - read
# a - add

# file = open('test.txt', 'w')
# file.write('Очень важная информация')
# file.close()

# fileR = open('test.txt', 'r')
# s = fileR.read()
# print(s)
# fileR.close()

name = input('Введите  свое имя: ')
fileA = open('test.txt', 'a')
fileA.write('\n' + name + ' hello!')
fileA.close()
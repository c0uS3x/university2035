# def summ(a, b):
#     s = a + b
#     return s     # Возвращаемое значение

def calc(a, b, operand):
    file = open('result.txt', 'a')
    result = 0
    if operand == '+':
        result = a + b
    elif operand == '-':
        result = a - b
    return result


num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
op = input('Введите операцию: ')

k = calc(num1, num2, op)
s = calc(1, 4, '+')
print(s)
print(k)

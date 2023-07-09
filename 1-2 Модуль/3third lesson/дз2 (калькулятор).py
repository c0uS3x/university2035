def calc(a, b, operand):
    file = open('result.txt', 'a')
    result = 0
    if operand == '+':
        result = a + b
    elif operand == '-':
        result = a - b
    elif operand == '*':
        result = a * b
    elif operand == ':':
        result = a / b
    return result


num1 = int(input('Введите число:'))
num2 = int(input('Введите число:'))
op = input('Введите операцию:')

res = calc(num1, num2, op)

file = open('result.txt', 'w')
file.write('\nПолучилось: ' + f'{res}')
file.close()
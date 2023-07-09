while True:
    a = float(input("введите 1 знак "))
    b = (input("введите действие "))
    c = float(input("введите 2 знак"))
if b == '+':
    print(a + c)
elif b == '-':
    print(a - c)
elif b == '*':
    print(a * c)
elif b == '/':
    print(a / c)
else:
    print("error")
input()

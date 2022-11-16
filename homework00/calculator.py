import typing as tp
from math import cos, tan, sin, log, pow


def kalc(a:float, command:str, b=1.0) -> tp.Union[float, str]:
    if command == '^2':
            return a ** 2
    if command == 'cos':
            return cos(a)
    if command == 'tan':
            return tan(a)
    if command == 'sin':
            return sin(a)
    if command == 'ln':
            return log(a)
    if command == 'lg':
            return log(a, 10)
    if command == '+':
            return a+b
    if command == '-':
            return a-b
    if command == '^':
            return pow(a, b)
    if command == '/':
        if b != 0:
            return a / b
        else: return 'На 0 делить нельзя'
    if command == '*':
            return a*b
    else: return 'Вы ввели какую-то ерунду'


print('Введите первое число:')
a = float(input())
print('Введите операцию')
command = input()
if command in ['^2', 'cos', 'tan', 'sin', 'ln', 'lg', '^']:
    print(kalc(a, command))
elif command in ['+', '-', '*', '/']:
    print('Введите второе число:')
    b = float(input())
    print(kalc(a, command, b))

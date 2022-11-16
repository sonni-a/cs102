import typing as tp
from math import cos, tan, sin, log, pow


def kalc(num_1: float, command: str, num_2=1.0) -> tp.Union[float, str]:
    if command == '^2':
        return num_1 ** 2
    if command == 'cos':
        return cos(num_1)
    if command == 'tan':
        if cos(num_1) == 0:
            return 'На 0 делить нельзя поэтому косинус не может быть равен нулю'
        return tan(num_1)
    if command == 'sin':
        return sin(num_1)
    if command == 'ln':
        if num_1 <= 0:
            return 'Аргумент должен быть больше нуля'
        return log(num_1)
    if command == 'lg':
        if num_1 <= 0:
            return 'Аргумент должен быть больше нуля'
        return log(num_1, 10)
    if command == '+':
        return num_1 + num_2
    if command == '-':
        return num_1 - num_2
    if command == '^':
        return pow(num_1, num_2)
    if command == '/':
        if num_2 == 0:
            return 'На 0 делить нельзя'
        return num_1 / num_2
    if command == '*':
        return num_1 * num_2
    return 'Вы ввели какую-то ерунду'


print('Введите первое число:')
num_1 = float(input())
print('Введите операцию')
command = input()
if command in ['^2', 'cos', 'tan', 'sin', 'ln', 'lg', '^']:
    print(kalc(num_1, command))
elif command in ['+', '-', '*', '/']:
    print('Введите второе число:')
    num_2 = float(input())_1, command, num_2))
    print(kalc(num_1, command, num_2))

import typing as tp
from math import cos, tan, sin, log, log1p, pow


def kalc(command):
    if command in ['^2', 'cos', 'tan', 'sin', 'ln', 'lg']:
        d = float(input())
        if command == '^2':
            return d **2
        if command == 'cos':
            return cos(d)
        if command == 'tan':
            return tan(d)
        if command == 'sin':
            return sin(d)
        if command == 'ln':
            return log1p(d)
        if command == 'lg':
            return log(d, 10)
    elif command in ['^', '+', '-', '/', '*']:
        a, b = map(float, input().split())
        if command == '+':
            return a+b
        if command == '-':
            return a-b
        if command == '^':
            return pow(a, b)
        if command == '/':
            return a / b
        if command == '*':
            return a*b
    else: return 'Вы ввели какую-то ерунду'


def calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    if command == "*":
        return num_1 * num_2
    if command == "/":
        return num_1 / num_2
    if command == '**':
        return num_1 ** num_2
    else:
        return f"Неизвестный оператор: {command!r}."


def match_case_calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    match command:
        case "*":
            return num_1 * num_2
        case "/":
            return num_1 / num_2
        case _:
            return f"Неизвестный оператор: {command!r}."
while True:

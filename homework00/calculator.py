import typing as tp
import math


operations_order = {0: ("^y",), 1: ("/", "*"), 2: ("+", "-")}


def convert(number: int, base: int) -> int:
    n = ''
    k = ''
    while number > 0:
        n = n + str(number % base)
        number = number // base
    n =  list(reversed(n))
    for j in range(len(n)):
        k += n[j]
    return k


def check_int(number: float) -> tp.Union[None, int]:
    """Проверка, что вещественное число преобразуется в целочисленное без потерь"""
    try:
        float(number)
    except ValueError:
        return False
    return True


def check_float(number: str) -> tp.Union[None, float]:
    """Проверка, что число вещественное"""
    try:
        float(str)
    except ValueError:
        return False
    return True


def check_input(number: str) -> float:
    """Проверка на ввод"""
    try:
        return float(number)
    except ValueError:
        return check_input(input("Повторите попытку > "))


def input_values(command: str) -> tuple[float, float] | tuple[float, None]:
    """Организация ввода одного или двух значений в зависимости от команды"""
    if command in ("+", "-", "*", "/", "#", "^y"):
        num_1 = check_input(input("Введите число 1 > "))
        num_2 = check_input(input("Введите число 2 > "))
        return num_1, num_2
    num = check_input(input("Введите число > "))
    return num, None


def calc(command: str, num_1: float, num_2=0.0) -> tp.Union[float, str]:  # type: ignore
    """Калькулятор операций"""
    if c == '+':
        return a + b
    if c == '-':
        return a - b
    if c == '*':
        return a * b
    if c == '/' and b == 0:
        return 'Делить на 0 нельзя'
    if c == '/' and b != 0:
        return a / b
    if c == '#' and b > 9:
        return 'Основание системы счисления должно быть не больше 9'
    if c == '#' and b <= 9 and check_int(a) is None or check_int(b) is None:
        return 'Число и основание системы счисления должны быть целочисленными'
    if c == '#' and b <= 9 and check_int(a) != None or check_int(b) != None:
        return convert(int(a), int(b))
    if c == '^y':
        return a ** b
    if c == '^2':
        return a ** 2
    if c == 'sin':
        return math.sin(num_1)
    if c == 'cos':
        return math.cos(num_1)
    if c == 'tg':
        return math.tan(num_1)
    if c == 'ln':
        return math.log(num_1)
    if c == 'log':
        return math.log10(num_1)
    else:
        return f"Неизвестная операция: {command!r}."


def parse_chain(chain: str):
    """Парсинг цепочки операторов до комбинации операторов и чисел"""
    chain = chain.replace(' ', '')
    chain = chain.replace('**', '^')
    new_chain = []
    if chain[0] == '-':
        cur_symbol = '-'
        chain = chain[1:]
    else:
        cur_symbol = ''
    for i, symbol in enumerate(chain):
        cur_symbol += symbol
        try:
            cur_symbol_f = float(cur_symbol)
            if i == len(chain) - 1:
                new_chain.append(cur_symbol_f)
        except ValueError:
            try:
                new_chain.append(float(cur_symbol[:-1]))
                if cur_symbol[-1] not in (set(operations_order[1]) | set(operations_order[2]) | {'^', '.'}):
                    print('Incorrect input!')
                    return None
                new_chain.append(cur_symbol[-1])  # type: ignore
                cur_symbol = ''
            except ValueError:
                print('Incorrect input!')
                return None
    return new_chain


def calc_order(order, chain: tp.List[tp.Union[str, float]]):
    """Вычисление операций текущего порядка"""
    for j, operator in enumerate(order):
        if operator[0] == len(chain) - 2:
            chain[operator[0] - 1 :] = [calc(operator[1], chain[operator[0] - 1], chain[operator[0] + 1])]
        else:
            if j != len(order) - 1:
                order[j + 1][0] -= (j + 1) * 2
            chain[operator[0] - 1 : operator[0] + 2] = [
                calc(operator[1], chain[operator[0] - 1], chain[operator[0] + 1])
            ]
    return chain


def solve_chain_wt_brackets(chain):
    """
    Вычисление цепочки операторов без скобок
    >>> solve_chain_wt_brackets('2 ** 3 ** 2 - 4.6 * 3 + 3 - 5 / 2 * 4 + 3 ** 3')
    70.2
    """

    chain = parse_chain(chain)
    if chain:
        chain = ['^y' if str(elem) == '^' else elem for elem in chain]
        order_0 = [[i, elem] for i, elem in enumerate(chain) if elem in operations_order[0]]
        chain = calc_order(order_0, chain)
        order_1 = [[i, elem] for i, elem in enumerate(chain) if elem in operations_order[1]]
        chain = calc_order(order_1, chain)
        order_2 = [[i, elem] for i, elem in enumerate(chain) if elem in operations_order[2]]
        chain = calc_order(order_2, chain)
        return chain[0]
    return None


def solve_brackets(chain):
    """Вычисление цепочки операторов со скобками
    >>> solve_brackets('((2 ** 3 ** 2 - (4.6 * (3 + 3) - 5) / 2 * 4) + 3 ** 3)')
    45.8
    """
    if chain.rfind('(') == 0 and chain.find(')') == len(chain) - 1:
        return solve_chain_wt_brackets(chain[1:-1])

    ob = chain.rfind('(')
    cb = chain.find(')')
    chain = chain[:ob] + str(round(solve_chain_wt_brackets(chain[ob + 1 : cb]), 2)) + chain[cb + 1 :]
    return solve_brackets(chain)


def solve_chain(chain: str) -> tp.Union[float, str]:
    """Проверка и вычисление цепочки операторов"""
    if chain.count('(') + chain.count(')') == 0:
        return solve_chain_wt_brackets(chain)
    if chain.count('(') != chain.count(')') or '()' in chain:
        return 'Невозможно выполнить!'
    chain = '(' + chain + ')'
    return solve_brackets(chain)


if __name__ == '__main__':
    while True:
        c = input('Введите операцию:')
        if c.isdigit() and int(c) == 0:
            break
        if len(c) <= 3:
            a, b = input_values(c)
            print(calc(c, a, b))
        else:
            print(solve_chain(c))

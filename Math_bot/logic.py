from operator import add, sub, mul, truediv


def operation(a: float, op: str, b: float) -> float:
    """ Считает арифметические операции для двух чисел и вернёт
        округлённый результат """
    opers = {'+': add, '-': sub, '*': mul, '/': truediv}
    callback = opers.get(op)
    if not callback:
        raise ArithmeticError('operator unknown')
    return round(callback(a, b), 2)


def get_list_elements(expression: str) -> list:
    """ Преобразует строку в список элементов
        example: '(1+2.2)*3' -> ['(', 1.0, '+', 2.2, ')', '*', 3.0]"""
    spam = ''
    massiv = []
    mass = []
    arr = []
    i = 0
    for symbol in expression:
        if symbol in '+-*/()':
            if spam:
                massiv.extend([float(spam), symbol])
            else:
                massiv.append(symbol)
            spam = ''
        elif symbol.isnumeric() or symbol == '.':
            spam += symbol
    else:
        if spam:
            massiv.append(float(spam))
    print(massiv)
    while i < len(massiv):
        if massiv[i - 1] == '-' and (massiv[i - 2] == '-' or massiv[i - 2] == '+' or massiv[i - 2] == '*' or massiv[i - 2] == '/' or massiv[i - 2] == '(') :
        # if massiv[i - 1] == '-' and massiv[i - 2] in "+-*/(": - не работает с float
            massiv[i] = massiv[i] * (-1)
            del massiv[i - 1]
        else:
            i += 1
        if massiv[0] == '-':
            massiv[1] = massiv[1] * (-1)
            del massiv[0]
    print(massiv)

    return massiv


def mass_operation(arr: list):
    """ Получает выражения уже без скобок и рекурсивно
        считает до конечного результата """
    for s in '*/+-':
        start = 0
        while s in arr:
            finish = len(arr) - 1
            try:
                idx = arr.index(s, start, finish)
                a, op, b = arr[idx - 1:idx + 2]
                result = operation(a, op, b)
                arr = arr[:idx - 1] + [result] + arr[idx + 2:]
                start = idx + 1
            except ValueError:
                break
    if not len(arr) > 1:
        if type(arr[0]) == "float":
            return int(arr[0])
        else:
            return arr[0]
    return mass_operation(arr)


def doing_simple(massiv: list) -> list:
    """ Извлекает из списка выражение в скобках, считает и заменяет
        результатом всё выражение в исходном списке """
    while '(' in massiv:
        for i in range(len(massiv) - 1, -1, -1):
            if not massiv[i] == '(':
                continue
            for j in range(i, len(massiv)):
                if not massiv[j] == ')':
                    continue
                result = mass_operation(massiv[i + 1:j])
                massiv = massiv[:i] + [result] + massiv[j+1:]
                break
    return massiv
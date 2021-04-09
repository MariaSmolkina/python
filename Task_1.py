# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def div_function(x, y):
    return x / y

values = list(input('Введите два числа через пробел: ').split())

try:
    print(f'Результат деления {values[0]} на {values[1]} : {div_function(float(values[0]), float(values[1])):.2}')
except ArithmeticError:
    print('Деление на 0')
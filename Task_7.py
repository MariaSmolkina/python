# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле
# необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial


def fact_func():
    for elem in count(1):
        yield factorial(elem)


try:
    user_number = int(input(f'Сколько чисел нужно вывести? Введите число: '))
except ValueError:
    print('Вы ввели не целое число')

counter = 1
for el in fact_func():
    if counter <= user_number:
        print(f'{counter}! = {el}')
        counter += 1
    else:
        break

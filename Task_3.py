# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# Если подразумевается, что в качестве аргументов выступают числа:
def my_func(x, y, z):
    mid_string = sorted([float(x), float(y), float(z)], reverse=True)
    return mid_string[0] + mid_string[1]

string_arguments = input('Введите три числа через пробел: ').split()

print(f'Сумма двух наибольших чисел: {my_func(string_arguments[0], string_arguments[1], string_arguments[2]):.2}')

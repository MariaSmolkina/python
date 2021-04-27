# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.
import traceback


class MyZeroDivisionError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Zero division error'
        else:
            return 'Zero division error has been raised'


first_value = int(input('Введите первое число: '))
second_value = int(input('Введите второе число: '))

try:
    if second_value == 0:
        raise MyZeroDivisionError
    else:
        print(f'Результат деления чисел: {first_value / second_value}')
except MyZeroDivisionError:
    print(traceback.format_exc())

# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.
import traceback


class Complex:

    def __init__(self, re, im):
        try:
            self.re = int(re)
            self.im = int(im)
        except ValueError:
            print(traceback.format_exc())

    def __str__(self):
        if self.im == 0:
            return f'{self.re}'
        elif self.re == 0:
            return f'{self.im}j'
        else:
            return f'{self.re} + {self.im}j'

    def __add__(self, other):
        self.re += other.re
        self.im += other.im
        return Complex(self.re, self.im)

    def __sub__(self, other):
        self.re -= other.re
        self.im -= other.im
        return Complex(self.re, self.im)

    def __mul__(self, other):
        result_re = self.re * other.re - self.im * other.im
        result_im = self.re * other.im + self.im * other.re
        return Complex(result_re, result_im).__str__()


complex_number_1 = Complex(1, 2)
complex_number_2 = Complex(1, 2)

# complex_number_1 = Complex(0, 2)
# complex_number_2 = Complex(0, 2)

# complex_number_1 = Complex(1, 0)
# complex_number_2 = Complex(1, 0)

try:
    print(f'Сумма двух чисел {complex_number_1} и {complex_number_2}: '
          f'{complex_number_1.__add__(complex_number_2).__str__()}')
    print(f'Разность двух чисел {complex_number_1} и {complex_number_2}: '
          f'{complex_number_1.__sub__(complex_number_2).__str__()}')
    print(f'Умножение двух чисел: {complex_number_1.__mul__(complex_number_2).__str__()}')
except AttributeError:
    print(traceback.format_exc())

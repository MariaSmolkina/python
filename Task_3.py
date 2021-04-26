# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
# исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, quantity):
        try:
            self.quantity = int(quantity)
        except ValueError:
            print('Not a number.')

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        result = self.quantity - other.quantity
        if result >= 0:
            return Cell(result)
        else:
            print('Вычитание невозможно, первая клетка меньше второй.')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        try:
            return Cell(self.quantity // other.quantity)
        except ZeroDivisionError:
            print('Деление на 0.')

    def make_order(self, cells_row_number):
        result = ''
        for _ in range(self.quantity // cells_row_number):
            result += f'{cells_row_number * "*"} \n'
        result += f'{self.quantity % cells_row_number * "*"}'
        return result

first_cell = Cell(7)
second_cell = Cell(5)
print(f'Результат сложения:\n{first_cell.__add__(second_cell).make_order(10)}')
print(f'Результат вычитания:\n{first_cell.__sub__(second_cell).make_order(10)}')
print(f'Результат умножения:\n{first_cell.__mul__(second_cell).make_order(10)}')
print(f'Результат деления:\n{first_cell.__truediv__(second_cell).make_order(10)}')

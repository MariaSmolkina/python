# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class MatrixException(BaseException):
    def __init__(self, first_user_matrix):
        self.first_matrix = first_user_matrix
        # print('Некорректно введены данные.')


class Matrix:

    def __init__(self, list_data_strings):
        self.strings = list_data_strings
        for count in range(len(self.strings)):
            if len(self.strings[count]) != len(self.strings[0]):
                raise MatrixException(self.strings)

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.strings])

    def __add__(self, other):
        result = []
        first_matrix_strings = len(self.strings)
        if first_matrix_strings != len(other):
            return 'Нельзя складывать матрицы с разной размерностью.'
        for count in range(first_matrix_strings):
            result.append([x + y for x, y in zip(self.strings[count], other[count])])
        return Matrix(result)


first_matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
second_matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
user_matrix = Matrix(first_matrix_data)
sec_user_matrix = Matrix(second_matrix_data)
print(f'Первая матрица:\n{user_matrix.__str__()}')
print(f'\nВторая матрица:\n{sec_user_matrix.__str__()}')
print(f'\nСумма двух матриц:\n{user_matrix.__add__(second_matrix_data)}')

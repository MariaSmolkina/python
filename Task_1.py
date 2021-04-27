# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, date_string):
        self.date = date_string

    @classmethod
    def date_from_str(cls, date_string):
        day, mon, year = map(int, date_string.split('-'))
        date_to_str = cls(f'{day}-{mon}-{year}')
        print(day, mon, year)

    @staticmethod
    def validation(date_string):
        day, mon, year = map(int, date_string.split('-'))
        if mon >= 12:
            print('Месяц должен быть от 1 до 12')
        if day >= 31:
            print('Число должно быть от 1 до 31')
        if year > 3000:
            print('Слишком далекое будущее)')


user_date = '10-08-1991'
Date.date_from_str(user_date)
Date.validation(user_date)

# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_function(f_name, l_name, date_birth, city, email, phone):
    print(f'Имя: {f_name}, '
          f'фамилия: {l_name}, '
          f'год рождения: {date_birth}, '
          f'город проживания: {city}, '
          f'email: {email}, '
          f'телефон: {phone}')

my_function(f_name='Tom', l_name='Tailor', date_birth=1991, city='Moskow', email='blabla@mail.ru', phone=888888888)
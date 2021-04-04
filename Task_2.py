
# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_time = int(input('Введите время в секундах:'))

hours = user_time // (60 * 60)
seconds_left = user_time % (60 * 60)
minutes = seconds_left // 60
seconds = seconds_left % 60

print(f'{hours}:{minutes}:{seconds}')
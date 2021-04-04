
# 1.1 Поработайте с переменными, создайте несколько, выведите на экран.

text = 'Hello'
name = 'Mary'
print(f'{text}, {name}!')

# 1.2 Запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

counter = 2
i = 0
value = [0] * counter
text_string = [0] * counter
while i < counter:
    value[i] = int(input('Введите число:'))
    text_string[i] = input('Введите текст:')
    i += 1
print(f'Введенные Вами числа: {value}')
print(f'Введенный Вами текст: {text_string}')

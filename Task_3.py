# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input('Введите число:')
n = int(user_number)
nn = int(user_number + user_number)
nnn = int(user_number + user_number + user_number)

print(f'Сумма = {n + nn + nnn}')
# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = abs(int(input('Введите целое положительное число:')))
max_number = 0
while user_number >= 1:
    if (user_number % 10) > max_number:
        max_number = user_number % 10
    user_number = user_number // 10

print(f'Самая большая цифра: {max_number}')
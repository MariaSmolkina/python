# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

num = 5
rand_list = [random.randint(0, 10 * num) for _ in range(num)]
min = rand_list[0]
max = rand_list[0]
max_pos = 0
min_pos = 0
spam = 0
for i in range(len(rand_list)):
    if min > rand_list[i]:
        min = rand_list[i]
        min_pos = i
    if max < rand_list[i]:
        max = rand_list[i]
        max_pos = i

print(f'Исходный массив: {rand_list}')
print(f'Максимум: {rand_list[max_pos]} в месте {max_pos}')
print(f'Минимум: {rand_list[min_pos]} в месте {min_pos}')

total_sum = 0
if min_pos < max_pos:
    for i in range(min_pos + 1, max_pos):
        total_sum += rand_list[i]
        i += 1
elif min_pos > max_pos:
    for i in range(max_pos + 1, min_pos):
        total_sum += rand_list[i]
        i += 1

print(f'Cумма элементов, находящихся между минимальным и максимальным элементами: {total_sum}')

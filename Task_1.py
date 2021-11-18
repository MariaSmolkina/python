# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

rand_list = [random.randint(0, 100) for _ in range(10)]
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

spam = rand_list[max_pos]
rand_list[max_pos] = rand_list[min_pos]
rand_list[min_pos] = spam

print(f'Массив после замены: {rand_list}')
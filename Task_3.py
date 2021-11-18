# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

num = 5
rand_list = [random.randint(0, num) for _ in range(num)]
min_list = [num + 1, num + 1]

for i in rand_list:
    if i <= min_list[0]:
        min_list.remove(min_list[0])
        min_list.append(i)
    if i <= min_list[1]:
        min_list.remove(min_list[1])
        min_list.append(i)

print(rand_list)
print(min_list)

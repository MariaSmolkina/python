# 4. Определить, какое число в массиве встречается чаще всего.

import random
import collections

a = [random.randint(0, 5) for _ in range(10)]

print(a)
y = collections.Counter(a)
print(y)

max_num = y[0]
for i in range(len(y)):
    if y[i] > max_num:
        max_num = y[i]

print(f'Число {[i for i in range(len(y)) if y[i] == max_num]} встречается чаще всех - {max_num} раз(а)')

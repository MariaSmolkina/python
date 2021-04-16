# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

numbers = [randint(0, 10) for i in range(5)]
line = ' '.join(map(str, numbers))
sum_numbers = 0

with open('task_5.txt', 'w+') as file:
        file.write(line)
        sum_numbers = sum(map(int, line.split()))

print(sum_numbers)

# Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import re
import statistics
import json

firms_dictionary = {}
keys = []
values = []
profit_values = []

with open('task_7.txt', 'r') as file:
    for line in file:
        keys.append(line.split(' ')[0])
        nums = [int(i) for i in re.findall(r'\d+', line)]
        profit = nums[1]-nums[2]
        values.append(profit)
        if profit > 0:
            profit_values.append(profit)

average_value = statistics.mean(profit_values)
average_profit = {'average_profit': average_value}

firms_dictionary = dict(zip(keys, values))
firms_data = [firms_dictionary, average_profit]
print(firms_data)

with open('firms_data_file.json', 'w') as data_file:
    json.dump(firms_data, data_file)



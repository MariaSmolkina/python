# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import statistics

salary = {}
min_salary_profile = []

with open('task_3.txt', 'r') as file:
    for line in file:
        text = line.split()
        salary[text[0]] = text[1]

for profiles in salary.keys():
    if int(salary[profiles]) < 20000:
        min_salary_profile.append(profiles)

min_salary_profile_string = ', '.join(min_salary_profile)

average_salary = statistics.mean(map(int, salary.values()))

print(f'Сотрудники, чей оклад менее 20 тыс.: {min_salary_profile_string}')
print(f'Средняя величина доходов сотрудников: {average_salary:.2f}')

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

number_dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
data = []

with open('task_4.txt', 'r') as read_file:
    for line in read_file:
        text = line
        first_value = line.split()[0]
        text = text.replace(first_value, number_dictionary.get(first_value))
        data.append(text)

with open('task_4_1.txt', 'w') as write_file:
    for el in data:
        write_file.write(el)

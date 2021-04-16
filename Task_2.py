# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task_2.txt', 'r') as file:
    count = 0
    for line in file:
        words_number = len(line.split())
        print(f'В {count+1} строке {words_number} слов')
        count += 1
print(f'В файле {count} строк')

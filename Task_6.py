# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
product_number = int(input('Введите количество единиц товара: '))

product_information = [0] * product_number
analytics_dictionary = {'Название': [],'Цена': [], 'Количество': [], 'Единица измерения': []}
characteristics_dictionary = {}
counter = 0
while counter < product_number:
    for dictionary_key in analytics_dictionary.keys():
        characteristics_dictionary[dictionary_key] = input(f'Введите {dictionary_key}:')
    product_information[counter] = (counter + 1, characteristics_dictionary)
    for dictionary_key in characteristics_dictionary.keys():
        analytics_dictionary[dictionary_key].append(characteristics_dictionary.get(dictionary_key))
    counter += 1

print(f'Структура данных "Товары":')
print(product_information)

print(f'Аналитика о товарах: ')
print(analytics_dictionary)
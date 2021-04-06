# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# # Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# # При нечетном количестве элементов последний сохранить на своем месте.
# # Для заполнения списка элементов необходимо использовать функцию input().

number = int(input('Введите число элементов списка: '))
new_list = list(range(number))
final_list = list(range(number))
for i in new_list:
    new_list[i] = input(f'Введите значение {i + 1}-го элемента: ')
counter = 0
if len(new_list) % 2 == 0:
    while counter < len(new_list):
        final_list[counter] = new_list[counter + 1]
        final_list[counter + 1] = new_list[counter]
        counter += 2
else:
    while counter < (len(new_list) - 1):
        final_list[counter] = new_list[counter + 1]
        final_list[counter + 1] = new_list[counter]
        counter += 2
    final_list[len(new_list) - 1] = new_list[len(new_list) - 1]
print(final_list)
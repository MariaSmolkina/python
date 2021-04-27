# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
from abc import ABC, abstractmethod
import traceback


class Storehouse:

    def __init__(self, s_id, address, dict_of_products):
        self.storehouse_id = s_id
        self.storehouse_address = address
        self.storehouse_products = dict_of_products

    @property
    def get_id(self):
        return self.storehouse_id

    @property
    def get_name(self):
        return self.storehouse_id

    @property
    def get_list_of_products(self):
        return self.storehouse_products

    def add_new_product(self):
        print('{color} Производится прием техники на склад {endcolor}'.format(color='\033[96m', endcolor='\033[0m'))
        while True:
            product_name = input('Введите название товара (для остановки введите stop): ')
            if product_name == 'stop':
                break
            try:
                product_count = int(input('Введите количество единиц товара: '))
            except ValueError:
                print(traceback.format_exc())
            try:
                sub_division_name = int(input(f'Укажите номер отдела (1, 2, 3) в который передается техника, '
                                          f'либо 4, если техника остается на складе:'))
            except ValueError:
                print(traceback.format_exc())
            try:
                if sub_division_name == 1:
                    SubDivision.add_equipment(first_subdivision, product_name, product_count)
                if sub_division_name == 2:
                    SubDivision.add_equipment(second_subdivision, product_name, product_count)
                if sub_division_name == 3:
                    SubDivision.add_equipment(third_subdivision, product_name, product_count)
                if sub_division_name == 4:
                    self.storehouse_products[product_name] = product_count
                else:
                    print('Неверно введены данные. Попробуйте еще раз:')
            except ValueError:
                print(traceback.format_exc())
        return self.storehouse_products


class OfficeEquipment(ABC):

    def __init__(self, name, price, description, store_id, discount, parameter):
        self.name = name
        try:
            self.price = int(price)
        except ValueError:
            print(traceback.format_exc())
            print('Некорректно введено значение цены.')
        self.description = description
        self.storehouse_id = store_id
        self.discount = discount
        self.parameter = parameter

    @property
    def get_name(self):
        return self.name

    @property
    def get_price(self):
        return self.price

    @property
    def get_storehouse_id(self):
        return self.storehouse_id

    set_discount = property()

    @set_discount.setter
    def set_discount(self, parameter):
        try:
            if int(parameter) < 0 or int(parameter) > 100:
                print('Некорректно введена величина скидки.')
            else:
                self.discount = int(parameter)
        except ValueError:
            print(traceback.format_exc())
            print('Некорректно введена величина скидки.')

    @property
    def get_discount(self):
        return self.discount

    def price_counter(self):
        try:
            total_price = self.price - self.price * (self.discount / 100)
            return f'Итоговая цена на {self.get_name} с учетом скидки {self.get_discount}%: {total_price} USD'
        except AttributeError:
            print(traceback.format_exc())
            print('Некорректно введена величина скидки.')


class Printer(OfficeEquipment):

    def get_print_speed(self):
        print(f'Скорость печати: {self.parameter} листов в минуту.')


class Scanner(OfficeEquipment):

    def get_scan_speed(self):
        print(f'Скорость сканирования: {self.parameter} листов в минуту.')


class Xerox(OfficeEquipment):

    def get_color_parameter(self):
        print(f'Тип цветопередачи: {self.parameter}.')


class SubDivision:

    def __init__(self, name, equipment_dict):
        self.name = name
        self.equipment_dict = equipment_dict

    def add_equipment(self, equipment_name, equipment_number):
        self.equipment_dict[equipment_name] = equipment_number
        return self.equipment_dict

    def get_list_of_equipment(self):
        return self.equipment_dict

    @property
    def get_name(self):
        return self.name


my_storehouse = Storehouse(1, 'My', {'Принтер': 1, 'Сканер': 1, 'Ксерокс': 1})
my_printer = Printer('Принтер', 100, 'Очень нужная вещь', 123, 0, 5)
my_scanner = Scanner('Сканер', 150, 'Тоже очень нужная вещь', 123, 0, 3)
my_xerox = Xerox('Ксерокс', 50, 'Не очень нужная вещь', 13, 0, 'multicolor')
first_subdivision = SubDivision('1', {'Компьютер': 1})
second_subdivision = SubDivision('2', {'Компьютер': 1})
third_subdivision = SubDivision('3', {'Компьютер': 1})

my_printer.set_discount = 15

print(my_printer.price_counter())
print(my_scanner.price_counter())
print(my_xerox.price_counter())

print(f'Товары на складе: {my_storehouse.storehouse_products}')
try:
    my_storehouse.add_new_product()
except UnboundLocalError:
    print(traceback.format_exc())

print(f'Товары на складе: {my_storehouse.storehouse_products}')

print(f'Товары в {first_subdivision.name} отделе: {first_subdivision.get_list_of_equipment()}')
print(f'Товары в {second_subdivision.name} отделе: {second_subdivision.get_list_of_equipment()}')
print(f'Товары в {third_subdivision.name} отделе: {third_subdivision.get_list_of_equipment()}')

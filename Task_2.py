# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    __length = None
    __width = None

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self, mass_square_meter, thickness):
        final_mass = self.__length * self.__width * mass_square_meter * thickness
        print(final_mass)


new_road = Road(20, 5000)
new_road.mass(25, 5)


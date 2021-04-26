# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class ClothesPiece(ABC):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def tissue_consumption_counter(self):
        pass

    set_parameter = property()

    @set_parameter.setter
    def set_parameter(self, parameter):
        self.parameter = parameter

    @property
    def return_parameter(self):
        return self.parameter


class Coat(ClothesPiece):

    def tissue_consumption_counter(self):
        coat_tissue_consumption = self.return_parameter / 6.5 + 0.5
        return coat_tissue_consumption


class Costume(ClothesPiece):

    def tissue_consumption_counter(self):
        costume_tissue_consumption = 2 * self.return_parameter + 0.3
        return costume_tissue_consumption


new_coat = Coat('пальто')
new_coat.set_parameter = 122
new_costume = Costume('костюм')
new_costume.set_parameter = 170
print(f'Расход ткани на {new_coat.name} размера {new_coat.return_parameter}: '
      f'{new_coat.tissue_consumption_counter():.2f}')
print(f'Расход ткани на {new_costume.name} для {new_costume.return_parameter} '
      f'роста: {new_costume.tissue_consumption_counter():.2f}')

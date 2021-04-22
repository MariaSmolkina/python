# Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'едет'

    def stop(self):
        return 'останавливается'

    def turn(self, direction):
        return f'поворачивает {direction}'

    def show_speed(self):
        return f'{self.speed} км/ч'


class TownCar(Car):
    def ___init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name)
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} км/ч (превышение скорости на {self.speed - 60} км/ч)'
        else:
            return f'{self.speed} км/ч'


class SportCar(Car):
    def ___init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name)
        self.is_police = is_police


class WorkCar(Car):
    def ___init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name)
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} км/ч (превышение скорости на {self.speed - 40} км/ч)'
        else:
            return f'{self.speed} км/ч'


class PoliceCar(Car):
    def ___init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


police_car = PoliceCar(80, 'белая', 'полицейская машина', True)
print(f'{police_car.color} {police_car.name} {police_car.go()} со скоростью {police_car.show_speed()}.')

fabia = TownCar(60, 'синяя', 'Fabia', False)
print(f'{fabia.color} {fabia.name} {fabia.go()} со скоростью {fabia.show_speed()}, а затем {fabia.turn("направо")}. ')

truck = WorkCar(50, 'желтый', 'грузовик', False)
print(f'{truck.color} {truck.name} {truck.go()} со скоростью {truck.show_speed()}.')

sport_car = SportCar(120, 'красный', 'спортивный авто', False)
print(f'{sport_car.color} {sport_car.name} {sport_car.go()} со скоростью {sport_car.show_speed()}.')

# Задание 1
import time


class TrafficLight:
    __color = ['КРАСНЫЙ', 'ЖЕЛТЫЙ', 'ЗЕЛЕНЫЙ']  # приватный атрибут класса

    def __running(self):  # метод класса
        times = [7, 2, 5]
        while True:
            for el in self.__color:
                print('\r' + el, end='')
                time.sleep(times[self.__color.index(el)])


a = TrafficLight()
a._TrafficLight__running()


# Задание 2
class Road:

    def __init__(self):
        self._length = float(input('Длина дороги, м: '))
        self._width = float(input('Ширина дороги, м: '))

    def _m_method(self, sp_mass=25, depth=5):
        return self._length * self._width * sp_mass * depth


b = Road()
print(f'Масса асфальта {b._m_method()} т.')

# Задание 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

p1 = Worker('Peter', 'Petrov', 'manager', 90000, 45000)
p2 = Position('Ivan', 'Ivanov', 'engineer', 100000, 50000)
print(p1.surname)
print(p1.position)
print(p1._income)
print(p2.position)
print(p2.get_full_name())
print(p2.get_total_income())

# Задание 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, new_speed):
        if new_speed > 0:
            self.speed = new_speed
            print(f'{self.color} автомобиль марки {self.name} поехал.')

    def stop(self):
        self.speed = 0
        print(f'{self.color} автомобиль марки {self.name} остановился.')

    def turn(self, direction):
        if direction == 'r' or direction == 'l':
            print(f'{self.color} автомобиль марки {self.name} повернул ', end='')
            print('направо.') if direction == 'r' else print('налево.')

    def show_speed(self):
        if self.speed > 0:
            print(f'{self.color} автомобиль марки {self.name} движется со скоростью {self.speed} км/ч.')
        else:
            print(f'{self.color} автомобиль марки {self.name} не движется.')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 0:
            print(f'{self.color} автомобиль марки {self.name} движется со скоростью {self.speed} км/ч.', end='')
            print(' Зарегистрировано превышение скорости!') if self.speed > 60 else print('\n')
        else:
            print(f'{self.color} автомобиль марки {self.name} не движется.')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 0:
            print(f'{self.color} автомобиль марки {self.name} движется со скоростью {self.speed} км/ч.', end='')
            print(' Зарегистрировано превышение скорости!') if self.speed > 40 else print('\n')
        else:
            print(f'{self.color} автомобиль марки {self.name} не движется.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


c1 = Car(120, 'Черный', 'Mazda', False)
c1.show_speed()
c1.stop()
c1.go(40)
c1.turn('r')
c1.show_speed()
print('*' * 12)
c2 = TownCar(80, 'Зеленый', 'Ford', False)
c2.show_speed()
c2.stop()
c2.show_speed()
print('*' * 12)
c3 = SportCar(180, 'Красный', 'Ferrari', False)
c3.show_speed()
c3.stop()
c3.go(100)
c3.turn('l')
c3.show_speed()
print('*' * 12)
c4 = WorkCar(0, 'Желтый', 'Kia', False)
c4.go(45)
c4.show_speed()
print('*' * 12)
c5 = PoliceCar(90, 'Серый', 'Lada', True)
c5.stop()
c5.go(90)
c5.show_speed()
print('*' * 12)

# Задание 5
class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Drawing.')

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Drawing with {self.title}.')

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Drawing with {self.title}.')

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Drawing with {self.title}.')

my_pen = Pen('black ink')
my_pen.draw()

my_pencil = Pencil('red pencil')
my_pencil.draw()

my_handle = Handle('blue handle')
my_handle.draw()

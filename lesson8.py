# Задание 1
class Date:
    def __init__(self, date_str='01-01-0001'):
        # date_str = 'Day-Month-Year'
        self.date_str = date_str
    @classmethod
    def date_extr(cls, date_str):
        return dict(zip(['Date', 'Month', 'Year'], list(map(int, date_str.split('-')))))
    @staticmethod
    def date_validation(date_str):
        max_date = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        DD = Date.date_extr(date_str).get('Date')
        MM = Date.date_extr(date_str).get('Month')
        YY = Date.date_extr(date_str).get('Year')
        err_count = 3
        if DD <= 0 or DD > max_date.get(MM):
            print(f'Day {DD} is invalid.', end=' ')
        else:
            err_count -= 1
        if MM <= 0 or MM > 12:
            print(f'Month {MM} is invalid.', end=' ')
        else:
            err_count -= 1
        if YY <= 0 or YY > 3000:
            print(f'Month {YY} is invalid.')
        else:
            err_count -= 1
        if err_count == 0:
            print(f'Date {date_str} is valid.')

print(Date.date_extr('30-6-1998'))
a = Date()
print(a.date_extr('31-7-2000'))

Date.date_validation('50-06-13900')
b = Date()
b.date_validation('4-05-2000')

# Задание 2
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
try:
    a = float(input('Input nominator: '))
    b = float(input('Input denominator: '))
    if b == 0:
        raise OwnError('Division by zero is undefined.')
except OwnError as err:
    print(err)
else:
    print(f'{a} / {b} =  {a / b}')

# Задание 3
class OwnTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []
num = input('Input number: ')
while num != 'stop':
    try:
        if set(num).issubset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}) and num != '':
            user_list.append(num)
        else:
            raise OwnTypeError("The entry is non-numeric.")
    except OwnTypeError as err:
        print(err)
    num = input('Input next number or "stop": ')
print(user_list)

# Задание 4 - 6

class EquipmentStore:
    def __init__(self):
        self.storage = []

    def accept(self, obj):
        return self.storage.append(obj)

    def transfer(self, obj):
        return self.storage.remove(obj)


class Equipment:
    i = 0

    def __init__(self, name, maker, model, place):
        self.name = name
        self.maker = maker
        self.model = model
        self.place = place
        self.__class__.i += 1


    @classmethod
    def get_inst_count(cls):
        return cls.i

    @property
    def create_unit(self):
        return {self.name: [self.maker, self.model, self.place]}



class Printer(Equipment):
    pass


class Scaner(Equipment):
    pass


class Xerox(Equipment):
    pass


store = EquipmentStore()
store.accept(Printer('printer', 'Hewlett-Packard', 'HP2000', 'A1').create_unit)
store.accept(Printer('printer', 'Hewlett-Packard', 'HP3000', 'A2').create_unit)
store.accept(Printer('printer', 'Hewlett-Packard', 'HP1000', 'A3').create_unit)
store.accept(Scaner('scaner', 'Epson', 'E300', 'B1').create_unit)
store.accept(Scaner('scaner', 'Epson', 'E300', 'B2').create_unit)
store.accept(Xerox('xerox', 'Xerox', 'X1200', 'C1').create_unit)
print(Printer.get_inst_count())
print(Scaner.get_inst_count())
print(Xerox.get_inst_count())
print(store)
store.transfer({'xerox': ['Xerox', 'X1200', 'C1']})
print(store)

# Задание 7

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b} * i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


z1 = ComplexNumber(3, -1)
z2 = ComplexNumber(1, 1)
print(str(z1))
print(str(z2))
print(str(z1 + z2))
print(str(z1 * z2))
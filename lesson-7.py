# Задание 1
class Matrix:
    def __init__(self, matrix):
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                print('Matrix strains should be the same size.')
            else:
                self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, self.matrix[i])) for i in range(len(self.matrix))])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print('The matrices should be the same size.')
        else:
            m = len(self.matrix)
            n = len(self.matrix[0])
            sum_matrix = [[self.matrix[i][j] + other.matrix[i][j] for i in range(m)] for j in range(n)]
            return Matrix(sum_matrix)

# Задание 2
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def consumption(self):
        return round(self.param * 2 + 0.3, 2)


art50 = Coat(44)
art100 = Suit(1.7)
print(art50.consumption)
print(art100.consumption)

# Задание 3
class Cell:

    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if Cell(self.n - other.n) != 0:
            return Cell(abs(self.n - other.n))
        else:
            return f'Subtraction is impossible.'

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(self.n // other.n)


    def make_order(self, unit):
        cell_strain = ''
        for i in range(int(self.n / unit)):
            cell_strain += '*' * unit + '\n'
        cell_strain += '*' * (self.n % unit)
        return cell_strain


c1 = Cell(51)
c2 = Cell(22)
print((c1 + c2).n)
print((c1 - c2).n)
print((c1 + c2).n)
print((c1 / c2).n)
print(c1.make_order(10))
print(c2.make_order(10))
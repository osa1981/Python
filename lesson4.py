# Задание 1
# Скрипт запускается из командной строки
from sys import argv
script_name, product_h, h_rate, bonus = argv
p = float(product_h)
r = float(h_rate)
b = float(bonus)
print(f'Заработная плата составляет {p * r + b} р.')
# Задание 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
gen_list = [i for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]  # генератор списка индексов нужных элементов
new_list = [my_list[i] for i in gen_list]  # генератор списка элементов по списку индексов
print(new_list)
# Задание 3
num_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(num_list)
# Задание 4
# решение через генератор, использующий встроенную функцию подсчета повторов каждого элемента в списке
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
# Задание 5
from functools import reduce
lst = [el for el in range(100, 1001, 2)]
# генератор списка четных чисел в диапазоне 100-1000 включительно
def my_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev * el
print(reduce(my_func, lst))
# Задание 6
from itertools import count
for el in count(3):
    if el > 10:
        break
    print(el)
from itertools import cycle
my_list = [1, "AB", "**", True]
с = 0
for el in cycle(my_list):
        if с > 3 * len(my_list) - 1:
            break  # останавливает цикл после того, как воспроизведет каждый элемент трижды
        print(el)
        с += 1
# Задание 7
from math import factorial
def fact(n):
    for i in range(1, n+1):
        yield factorial(i)
def f_func(n):
    for el in fact(n):
        print(el)
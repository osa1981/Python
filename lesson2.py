# Задача 1
my_list = ['Frank', 'K.C.', 12, 'Apr', 1956, 34569.87, True, None]
for el in my_list:
    print(type(el))
# Задача 2
pre_li = input('Введите список, разделяя элементы пробелом: ')
li = pre_li.split()
for i in range(1, (2 * (len(li) // 2) + 1), 2):  # проходит по индексам на четных позициях
    li[i - 1], li[i] = li[i], li[i - 1]   # меняет соседние элементы местами
print(li)
# Задача 3, решение через list
s_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
season = ['зима', 'весна', 'лето', 'осень']
month = int(input('Введите номер месяца: '))
if month <= 12 and month >= 1:
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            if s_list[i][j] == month:
                s = i
    print(f'Время года - {season[s]}')
else:
    print('Ошибка ввода данных')
# Задача 3, решение через dict
s_dict = {'зима':[12, 1, 2], 'весна':[3, 4, 5], 'лето':[6, 7, 8], 'осень':[9, 10, 11]}
month = int(input('Введите номер месяца: '))
for s in s_dict:
    if month in s_dict[s]:
        print(f'Время года - {s}')
# Задача 4
my_list = input('Введите строку: ').split()
for ind, el in enumerate(my_list, 1):
    print(ind, el[:10])
# Задача 5
my_list = [9, 8, 6, 6, 4, 2, 2, 2, 1]
rate = int(input('Введите значение рейтинга: '))
i = 0
while rate < my_list[i]:
    i += 1
my_list.insert(i, rate)
print(my_list)
# Задача 6
num = int(input('Введите количество наименований товаров: '))
num_list = []
for x in range(num):
    num_list.append(x + 1)   # создает список номеров товаров
param_list = input('Введите список параметров товара через запятую: ')
param_list = param_list.split(',')  # создает список параметров товара
my_list = []  # объявляет таблицу данных
for el in num_list:
    param_dict = {}  # объявляет словарь для заполнения значениями параметров ("карточку товара")
    for i in range(len(param_list)):
        param_dict[param_list[i]] = input(f'{param_list[i]} товара {el}: ')  # заполняет "карточку товара" значениями
    my_list.append((el, param_dict))
my_dict = {}   # объявляет целевой словарь
my_dict.fromkeys(param_list)  # заполняет ключами - параметрами товара
for p in param_list:
    l = []  # список, куда будут записываться значения параметра p
    for x in my_list:
        m_dict = x[1]   # поочередно помещает карточки товаров из таблицы в m_dict
        l.append(m_dict.get(p))   # заполняет список l значениями p
    my_dict[p] = list(set(l))
print(my_dict)
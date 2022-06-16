# Задание 1
f_name = input('Введите имя файла: ')
with open(f_name, 'w') as my_file:
    f_str = input('Вводите содержимое файла построчно. Завершите файл пустой строкой.\n: ')
    while True:
        if f_str != '':
            my_file.write(f_str + '\n')
            f_str = input(': ')
        else:
            break
# Задание 2
with open('list1.txt', 'r') as my_file:
    f_dict = {}
    s_num = 0  # номер текущей строки
    for line in my_file:
        li = line.split()
        w = len(li)  # количество слов в каждой строке
        print(w)
        s_num += 1
        f_dict.update({s_num: w})
print(f'Количество строк в файле - {s_num}.')
for key, value in f_dict.items():
    print(f'Количество слов в строке {key} равно {value}.')
# Задание 3
f_dict = {}
m = 0  # суммирование зарплат и вычисление среднего
n = 0  # число сотрудников с указанием зарплаты
low_list = []
err_list = []
with open('list1.txt', 'r', encoding="utf8") as my_file:
    for line in my_file:
        try:
            row = line.split()
            f_dict.update({row[0]: row[1]})
        except IndexError:
            pass  # игнорирует пустые или неполные строки
    for key in f_dict:
        try:
            v = float(f_dict.get(key))
            m = m + v
            n += 1
            low_list.append(key) if v < 20000 else None
        except ValueError or TypeError:
            err_list.append(key)
m = m / n
print(f'Средняя величина доходов сотрудников составляет {round(m, 2)}.')
if len(low_list) == 0:
    print('Сотрудников с зарплатой ниже 20000 не обнаружено.')
else:
    print('Сотрудники с зарплатой ниже 20000:')
    for el in low_list:
        print(el)
if len(err_list) != 0:
    print('Сотрудники, зарплатные данные которых введены некорректно:')
    for el in err_list:
        print(el)
# Задание 4
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('list1.txt', 'r', encoding='utf-8') as in_file:
    for line in in_file:
        if line[-1] == '\n':
            new_list.append(my_dict.get(line[:-5]) + line[-4:])
        else:
            new_list.append(my_dict.get(line[:-4]) + line[-3:])
with open('list2.txt', 'w', encoding='utf-8') as out_file:
    out_file.writelines(new_list)
# Задание 5
with open('my_data.txt', 'w') as num_file:
    f_str = input('Вводите числа, разделяя пробелом:\n')
    num_file.write(f_str)
li = f_str.split()
try:
    resume = sum(map(lambda x: int(x), li))
    print(f'Сумма чисел в файле равна {resume}.')
except ValueError:
    print('Введенная последовательность содержит нечисловые данные')
# Задание 6
subj_dict = {}
with open('shedule.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        char_list = list(line)
        new_str = str()
        for el in char_list:  # записывает в строку только числовые символы, сохраняя пробелы
            if ord(el) < 57 and ord(el) > 47 or ord(el) == 32:
                new_str = new_str + el
        s = sum(map(int, new_str.split()))  # вычисляет сумму часов для предмета
        subj_dict.update({line.split(':')[0]: s})  # извлекает название предмета и добавляет
        # как ключ в словарь
print(subj_dict)
# Задание 7
profit_list = {}  # словарь прибыльных фирм с прибылями
loss_list = {}  # словарь убыточных фирм с убытками
with open('my_data.txt', 'r', encoding='utf-8') as f_obj:
    n_profit = 0  # число прибыльных фирм
    n_loss = 0  # число убыточных фирм
    for line in f_obj:
        firm_name, prop_form, revenue, costs = line.split()
        profit = float(revenue) - float(costs)
        if profit >= 0:
            profit_list.update({firm_name: profit})
            n_profit += 1
        else:
            loss_list.update({firm_name: abs(profit)})
            n_loss += 1
    mean_profit = sum(map(float, profit_list.values())) / n_profit
    mean_loss = sum(map(float, loss_list.values())) / n_loss
report = []  # отчетный список
report.append({'прибыльные компании': profit_list})
report.append({'средняя прибыль': mean_profit})
report.append({'убыточные компании': loss_list})
report.append({'средний убыток': mean_loss})
import json
with open('my_file.json', 'w') as js_f:
    json.dump(report, js_f)


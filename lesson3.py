# Задание 1
def div_func(a1, a2):
    ''' Возвращает частное от деления двух чисел

    a1 - делимое, a2 - делитель
    >>> (float, float) -> float
    '''
    try:
       a1 / a2
    except ZeroDivisionError:
        return 'Ошибка, попытка деления на 0'
    return a1 / a2
a1 = float(input('Введите делимое: '))
a2 = float(input('Введите делитель: '))
print(div_func(a1, a2))
# Задание 2
def my_func(
        name,
        surn,
        birth='1990',
        city='Москва',
        email=None,
        phone=None
):
    return print(f'{name}, {surn}, {birth}, {city}, {email}, {phone}')
my_func(name='Анна', surn='Иванова', email='aivanova@gmail.ru', phone='8(495)1234567')
# Задание 3
def my_func(num1, num2, num3):
    '''Возвращает сумму двух наибольших чисел из трех введенных

    (float, float, float) -> float
    '''
    li = [num1, num2, num3]
    li_sort = sorted(li, reverse=True)
    return li_sort[0] + li_sort[1]
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = float(input('Введите третье число: '))
print(my_func(num1, num2, num3))
# Задание 4
def my_func(x = 1, y = -1):
    '''Возводит положительное число в отрицательную степень'''
    while True:
        try:
            x = float(input('Введите основание - положительное действительное число: '))
            y = int(input('Введите степень - отрицательное целое число: '))
            break
        except ValueError:
            print('Ошибка ValueError. Повторите ввод')
    res = 1
    for i in range(abs(y)):
       res = res * (1 / x)
    if x <= 0 or y > 0:
        print('Ошибка: знак аргумента(ов)')
    else:
        return res
print(my_func())
# Задание 5
def my_func(*args):
    print('Вводите числа одной строкой через пробел. Для ввода нажмите Enter. Чтобы завершить программу, введите #')
    s = 0
    while True:
        li = input().split()
        for el in li:
            try:
                el = float(el)
                s = s + el
            except ValueError:
                if el == '#':
                    return print(f'Сумма равна {s}')
                else:
                    return print('Ошибка: неизвестный символ')
        print(f'Сумма равна {s}')
my_func()
# Задание 6
def int_func(x):
    return x.capitalize()
print(int_func(input('Введите слово: ')))
# Задание 7
text = input('Введите строку: ').split()
for i in range(len(text)):
    text[i] = int_func(text[i])
print(' '.join(text))
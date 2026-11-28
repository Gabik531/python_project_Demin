# Вариант 11. Задание 2.
# Дано число R и список A размера N.
# Найти элемент списка, наиболее близкий к числу R,
# для которого величина |AK - R| минимальна.


import random

try:
    n = int(input('Введите размер списка: '))
    r = float(input('Введите число R: '))

    if n > 0:
        a = []
        for i in range(n):
            a.append(random.randint(-100, 100))

        print('Исходный список:', a)

        nearest = a[0]
        for element in a:
            if abs(element - r) < abs(nearest - r):
                nearest = element

        print('Ближайший элемент:', nearest)
    else:
        print('Размер списка должен быть положительным.')
except ValueError:
    print('Ошибка: необходимо ввести число.')

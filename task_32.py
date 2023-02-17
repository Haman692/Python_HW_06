# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list = [random.randint(-10, 10) for i in range(20)]
print(list)
minNumber = int(input('Минимальное значение = '))
maxNumber = int(input('Максимальное значение = '))
for i in range(len(list)):
    if minNumber <= list[i] <= maxNumber:
        print(i + 1)
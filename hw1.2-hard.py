#!/usr/bin/env python3
# coding: utf-8

# Задание-1.2:
# Найдите n-ое число Фибоначчи

def FiboNumber(x):
    if x > 2:
        a = 0
        b = 1

        for y in range(3, x +1):
            c = a+b
            a = b
            b = c

        print (str(c))

    else:
        print ('Количество элементов ряда должно быть больше двух')

# ------------------------------------------------------------------------------------------------------

#FiboNumber(int(10))

nmbr = input('Введите количество элементов ряда: ')
FiboNumber(int(nmbr))

#!/usr/bin/env python3
# coding: utf-8

# Задание-1.1:
# Пользователь вводит число определите, является ли данное число простым.
# Делится только на себя и на единицу

def SimpleNumber(x):
    res = True

    if x > 1:
        for y in range(2, x - 1):
            if x % y == 0: # Если проверяемое число разделилось без остатка на число из цикла
                res = False
                break
    else:
        print ('Проверяемое число должно быть больше единицы')
        res = False

    return res

# ------------------------------------------------------------------------------------------------------

nmbr = input('Введите число для проверки: ')

if SimpleNumber(int(nmbr)) == True:
    print('Проверяемое число является простым')
else:
    print('Проверяемое число не является простым')
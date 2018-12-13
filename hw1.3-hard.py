#!/usr/bin/env python3
# coding: utf-8

# Задание-1.3:
# Пользователь вводит n и m и нужно вывести на экран:
# AAABBBAAABBBAAABBB
# BBBAAABBBAAABBBAAA
# AAABBBAAABBBAAABBB
# Для этого примера n ==3, m == 3
# где n - это количество строк, m - это кол-во троек ААА в одной строке

# ------------------------------------------------------------------------------------------------------

def MixStr (str1, str2, repeat_count, mode):
    res = ''

    for i in range(1, repeat_count +1):
        if mode == 0:
            res = res + str1 + str2
        if mode == 1:
            res = res + str2 + str1

    return res

def Xz(n, m):
    if (n > 0) and (m > 0):
        a_str = 'AAA'
        b_str = 'BBB'

        for x in range(1, n +1):
            if x % 2 == 0: # Если номер строки чётный
                print (MixStr (a_str, b_str, m, 1))
            else:
                print (MixStr (a_str, b_str, m, 0))
    else:
        print ('Количество должно быть больше ноля')

# ------------------------------------------------------------------------------------------------------

#n = 10
#m = 7

n = int(input('Введите количество строк: '))
m = int(input('Введите количество повторов "ААА": '))

Xz(n, m)

#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.

#    Y   Z
#    |  /
#    | /
#    |/______X
#    0

# 0- непрозрачный кубик, 1- прозрачный
# Порядо координат Z Y X
# Куб "рисуется" с нижней левой точки

import random
# -----------------------------------------------------

matrix = []
n = 3 # размерность матрицы
# -----------------------------------------------------

for i in range(n):
    smatrix = []
    for j in range(n):
        ssmatrix = []
        for k in range(n):
            ssmatrix.append(random.randint(0, 1))
            #ssmatrix.append(0)
        smatrix.append(ssmatrix)
    matrix.append(smatrix)

#      z  y  x
#matrix[0][0][0] = 1
#
for z in range (n):
    print('')
    print('Z: ' + str(z)) # нумерация от наблюдателя (срез/слой/ряд)
    print('')
    for y in range(n):
        for x in range(n):
            print (f'{matrix[z][n -y -1][x]:<3}', end = '')
        print('')
#
print('')
print('Результат: ')
print('')
#
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == 0: # Смотрим по оси Z
                z = 0
                y = j
                x = k
                if matrix[z][n -y -1][x] == 1:
                    sum = 1
                    road = 'Z:' + str(z) + ' Y:' + str(n -y -1) + ' X:' + str(x) + ' > '
                    for zz in range(1, n, 1):
                        if matrix[zz][n -y -1][x] == 1:
                            sum += 1
                            road = road + 'Z:' + str(zz) + ' Y:' + str(n -y -1) + ' X:' + str(x) + ' > '
                        else:
                            break

                        if sum == n:
                            road = road[0:len(road) - 3]
                            print ('Z ---> '+road)
            #
            if i == 1: # Смотрим по оси Y
                z = j
                y = 0
                x = k
                if matrix[z][y][x] == 1:
                    sum = 1
                    road = 'Z:' + str(z) + ' Y:' + str(y) + ' X:' + str(x) + ' > '
                    for yy in range(1, n, 1):
                        if matrix[z][yy][x] == 1:
                            sum += 1
                            road = road + 'Z:' + str(z) + ' Y:' + str(yy) + ' X:' + str(x) + ' > '
                        else:
                            break

                        if sum == n:
                            road = road[0:len(road) - 3]
                            print ('Y ---> '+road)
            #
            if i == 2: # Смотрим по оси X
                z = k
                y = j
                x = 0
                if matrix[z][n -y -1][x] == 1:
                    sum = 1
                    road = 'Z:' + str(z) + ' Y:' + str(n -y -1) + ' X:' + str(x) + ' > '
                    for xx in range(1, n, 1):
                        if matrix[z][n -y -1][xx] == 1:
                            sum += 1
                            road = road + 'Z:' + str(z) + ' Y:' + str(n -y -1) + ' X:' + str(xx) + ' > '
                        else:
                            break

                        if sum == n:
                            road = road[0:len(road) - 3]
                            print ('X ---> '+road)

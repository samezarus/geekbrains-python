#!/usr/bin/env python3
# coding: utf-8

# EXTRA
# Есть два словаря. Один это рецепт блюда, второй это список продуктов, которые есть в ходильнике.
#
# Ключ это название продукта, значение - это количество.
#
# Нужно сравнить два словаря и дать словарь, в котором будет список покупок
# Если для рецепта всё есть, то сказать что ничего не нужно
# Разницей по измерению гр, мл, шт. Пренебречь

# Рецепт акрошки
#Prescription = {1: 11, 2: 12, 3: 13}
Prescription = {}
Prescription['Квас']      = 3
Prescription['Огурцы']    = 10
Prescription['Яйца']      = 15
Prescription['Лук']       = 0.5
Prescription['Сосиски']   = 2
Prescription['Картофель'] = 1
Prescription['Редис']     = 1
Prescription['Соль']      = 0.1
Prescription['Сахар']     = 0.2

# Продукты в холодильнике
ProductsInBox = {}
ProductsInBox['Квас']      = 1.5
ProductsInBox['Огурцы']    = 3
ProductsInBox['Яйца']      = 10
ProductsInBox['Лук']       = 0
ProductsInBox['Сосиски']   = 1
ProductsInBox['Картофель'] = 0
ProductsInBox['Редис']     = 0.1
ProductsInBox['Соль']      = 1
ProductsInBox['Сахар']     = 1

# Список покупок
ShoppingList = {}

print ('Рецепт акрошки:')
for item in Prescription:
    key   = item
    value = Prescription.get(item)

    ShoppingList[key] = value

    print ('    ' + key + ': ' + str(value))

print ('---------------------------------')

print ('Продукты в холодильнике:')
for item in ProductsInBox:
    key   = item
    value = ProductsInBox.get(item)

    value2 = ShoppingList.get(key) # Ищем в холодильнике количество продукта из рецепта
    if value2 != None:
        i = value2 -value
        if i > 0:
            ShoppingList[key] = i
        if i < 0:
            ShoppingList[key] = 0

    print ('    ' + key + ': ' + str(value))

print ('---------------------------------')

print ('Список покупок:')
for item in ShoppingList:
    key   = item
    value = ShoppingList.get(item)
    print ('    ' + key + ': ' + str(value))
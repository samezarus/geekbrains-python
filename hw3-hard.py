#!/usr/bin/env python3
# coding: utf-8

# Задание-1

# Написать консольное меню вида:

# 1. Добавить
# 2. Удалить
# 3. Распечатать
# 4. Посчитать
# 5. Выйти

# Надо чтобы
# а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
# б) Каждое действие (добавить, удалить и тд) должно быть функцией
# в) У пользователя надо спросить номер команды
# г) Программа не должна завершаться пока не введется команда Выйти
# д) Проверять на ввод ошибочных данных, там где они могут появиться

import os
import time

def StrIsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def ClearScren():
    #os.system('clear') # nix
    os.system('cls') # win

class TMainMenu:

    Items = []
    Functions = []
    ExitCode = 0

    def __init__(self):
        pass

    def AddItem(self, Caption):
        self.Items.append(Caption)

    def PrintItems(self):
        ClearScren()
        for i in range(len(self.Items)):
            print(str(i + 1) + '. ' + self.Items[i])

    def ItemClick (self, index, txt):
        self.Functions[index](txt)

# ------------------------------------------------
MainMenu = TMainMenu()
MainMenu.ExitCode = 5
#
Captions = []
Captions.append('Добавить')
Captions.append('Удалить')
Captions.append('Распечатать')
Captions.append('Посчитать')
Captions.append('Выйти')
# Только не надо мне говорить, что функции одинаковые ) Лёгким движением руки они смогут выполнять различные действия :P
def FAdd (val):
    print('>  Действие "' + val + '" выполнено')
def FDelete (val):
    print('>  Действие "' + val + '" выполнено')
def FPrint (val):
    print('>  Действие "' + val + '" выполнено')
def FCalc (val):
    print('>  Действие "' + val + '" выполнено')
def FExit (val):
    print('>  Действие "' + val + '" выполнено')
#
MainMenu.Functions.append(FAdd)
MainMenu.Functions.append(FDelete)
MainMenu.Functions.append(FPrint)
MainMenu.Functions.append(FCalc)
MainMenu.Functions.append(FExit)
#
for i in range(len(Captions)):
    MainMenu.AddItem(Captions[i])
#
value = 0
while value != MainMenu.ExitCode:
    MainMenu.PrintItems()
    s = input('Выберите нужный пунк меню: ')

    if StrIsInt(s) is True:
        value = int(s)

        if (value < len(MainMenu.Items) + 1) and (value > 0):
            print('')
            MainMenu.ItemClick(value -1, MainMenu.Items[value -1])
            time.sleep(1)
        else:
            print('')
            print ('>  Введён не верный пунк меню')
            time.sleep(1)
    else:
        print('')
        print ('>  Пунк меню может быть только числом')
        time.sleep(1)

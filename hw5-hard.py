#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys

#def getOSType():
#    res = 0 # nix
#    if os.name == 'nt':
#        res = 1 # win
#    return res

def cpFunc ():
    if os.path.isfile (currentDir+dir_name):
        os.system('cp '+currentDir+dir_name+' '+currentDir+'copy-'+dir_name)
        print ('Файл "'+dir_name+'" скопирован')
    else:
        print ('Файл "' + dir_name + '" не существует')

def rmFunc ():
    if os.path.isfile (dir_name):
        os.remove(dir_name)
        print ('Файл "'+dir_name+'" удалён')
    else:
        print ('Файл "' + dir_name + '" не существует')

def cdFunc ():
    if os.path.exists(dir_name):
        currentDir = dir_name
        print ('Текущая директория изменена на: ' + currentDir )
    else:
        print ('Директория "'+dir_name+'" не существует')

def lsFunc ():
    print ('Текущая директория: ' + currentDir)


print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создние копии указанного файла")
    print("rm <file_name>  - удаление указанного файла")
    print("cd <full_path or relative_path> - измение текущий директории на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cpFunc,
    "rm": rmFunc,
    "cd": cdFunc,
    "ls": lsFunc
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    currentDir = sys.path[0]+'/'
except IndexError:
    currentDir = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

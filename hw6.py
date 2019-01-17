#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Задание-2:
#
# Написать класс, который будет удобно использовать для
# работы с (на выбор что-нибудь одно):
# комплексными числами \ матрицами \ светофор \ микроволновка

# Cветофор:

class TLights:
    pCurentColor = ''
    ################################
    def __init__(self):
        """Constructor"""
    #
    def showRed(self):
        self.pCurentColor = 'red'
        print ('\x1b[0;37;41m' + '  ' + '\x1b[0m')
    #
    def showYellow(self):
        self.pCurentColor = 'yellow'
        print ('\x1b[0;37;43m' + '  ' + '\x1b[0m')
    #
    def showGreen(self):
        self.pCurentColor = 'green'
        print ('\x1b[0;37;42m' + '  ' + '\x1b[0m')
    #
    def showGrey(self):
        print ('\x1b[0;37;47m' + '  ' + '\x1b[0m')
    #
    def showLights(self, _color):
        if _color == 'red':
            self.showRed()
            self.showGrey()
            self.showGrey()

        if _color == 'yellow':
            self.showGrey()
            self.showYellow()
            self.showGrey()

        if _color == 'green':
            self.showGrey()
            self.showGrey()
            self.showGreen()

Lights = TLights()

Lights.showLights('green')

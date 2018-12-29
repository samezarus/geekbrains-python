#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.

import os.path
#
FilePath = 'pwd.txt'
PassDict = dict()
MaxCount = 0
PlaceNamber = 1
MaxPlaces = 10
CountInPlace = 0
#
if os.path.isfile(FilePath):
    file = open(FilePath, 'r')
    #
    for line in file:
        pos = line.find(';')
        #
        if pos != -1:
            pswd = line[pos +1:].strip()
            #
            if len(pswd) > 0:
                if PassDict.get(pswd) != None:
                    count = PassDict[pswd] +1
                else:
                    count = 1
                #
                if count > MaxCount:
                    MaxCount = count

                #
                PassDict.update({pswd: count})
    #
    if len(PassDict) > 0:
        for i in range (len(PassDict)):
            if MaxCount > 0 and PlaceNamber <= MaxPlaces :
                CountInPlace = 0
                #
                for KeyVal in PassDict:
                    if PassDict[KeyVal] == MaxCount:
                        print ('Место № ' + str(PlaceNamber) + ' "' + str(KeyVal) + '" Количество: ' + str(MaxCount))
                        CountInPlace += 1
                #
                if CountInPlace > 0 :
                    PlaceNamber += 1
                    print ('---------------------------------------------')
            else:
                break
            #
            MaxCount -=1
        #
        #for KeyVal in PassDict:
        #    print (str(KeyVal) + ':' + str(PassDict[KeyVal]))
else:
    print('Не удалось найти файл "'+FilePath+'"')
#

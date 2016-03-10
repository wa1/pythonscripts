# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:41:57 2016

@author: erik.lundin
"""

import urllib.request
import json

conversionUrl = "http://api.fixer.io/latest?base={}"
currencyNamesUrl = "https://openexchangerates.org/api/currencies.json"
currencyNamesJson = urllib.request.urlopen(currencyNamesUrl).read().decode('utf-8')
currencyNames = json.loads(str(currencyNamesJson))

a = input('Konvertera från: ')
a = a.upper()
print(a + ': ' + currencyNames[a])

b = input('till: ')
b = b.upper()
print(b + ': ' + currencyNames[b])

c = float(input('Antal ' + a + ':'))

currencyJson = urllib.request.urlopen(conversionUrl.format(a)).read().decode('utf-8')
currency = json.loads(str(currencyJson))
print('Resultat: ' + str(c) + ' ' + a + ' = ' + str(currency['rates'][b] * c) + ' ' + b)
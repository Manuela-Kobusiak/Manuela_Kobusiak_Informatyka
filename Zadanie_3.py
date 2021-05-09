# -*- coding: utf-8 -*-
"""
Created on Sun May  9 08:29:42 2021

@author: Manuela
"""

a = 1
b = 10
suma = 0
i = 0
if a % 2 == 0:
    a = a + 1
    print(a)
else:
    print(a)
while a <= b:
    suma = suma + a
    i = i + 1
    a = a + 2
srednia = suma / i
print (srednia)

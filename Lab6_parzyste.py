# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:10:48 2021

@author: Manuela
"""

zmienna=input('wprowadz wartosc = ')
x=int(zmienna)
for i in range(-x,x+1):
    if(i % 2 == 0):
        print(i)
        
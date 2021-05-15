# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:38:08 2021

@author: Manuela
"""

lista=[2,7,5,6,4,8,3,1]
n=len(lista)
for i in range(0,n-1):
    for j in range(i+1,n):
        if lista[i]>lista[j]:
            maks=lista[i]
            lista[i]=lista[j]
            lista[j]=maks
       print(lista)    

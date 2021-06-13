# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:12:08 2021

@author: 
"""
 
import smtplib, ssl

def WyslijWiadomosc(serwer,port,nadawca,haslo,wiadomosc):
    try:
        ssl_pool=ssl.create_default_context()
        with smtplib.SMTP_SSL(serwer,port,context=ssl_pool) as serwer:
            serwer.login(nadawca,haslo)
            serwer.sendmail(nadawca,odbiorca,wiadomosc)
        print("Wiadomosc wyslana pomyslnie!")
    except:
        print("Nie udalo sie wyslac wiadomosci! : ")


port=465
serwer="smtp.gmail.com"
nadawca="wimimprojekt@gmail.com"
haslo="yuxjyaazdouprhun"

odbiorca=input("Podaj odbiorcę: ")
temat=input("Podaj temat wiadomosci: ")
wiadomosc1=input("Podaj wiadomosc: ")
potwierdzenie=input("Czy na pewno chcesz wysłać wiadomosc do "+odbiorca+" ? (wpisz tak(t) lub nie(n))")

wiadomosc="Subject:"+temat+"\nFROM: Informatyka projekt\n"+wiadomosc1


if potwierdzenie == "tak" or potwierdzenie == "Tak" or potwierdzenie == "t" or potwierdzenie == "T":
    WyslijWiadomosc(serwer,port,nadawca,haslo,wiadomosc)
elif potwierdzenie == "nie" or potwierdzenie == "Nie" or potwierdzenie == "n" or potwierdzenie == "N":
    print("Nie wysłano wiadomosci!")
    
    



    


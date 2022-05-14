# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:32:30 2022

@author: Dawid Borawski
"""

lista = [0,2,1,3,7,4]
print(lista)
lista.append(5)
print(lista)
lista.extend([6,8,9,10])
print(lista)

dict = {
        "imie" : "dawid",
        "nazwisko" : "borawski"
        }

print(dict)
print(dict.keys())
print(dict.values())

print(bool( ))
print(bool(''))
print(bool(0))
print(bool(1))
print(bool('0'))
print(bool('1'))
print(bool([]))
print(bool([","]))

i=0
while i < 21:
    print(i)
    i += 1


napis = "Ala ma kota i psa"
temp = ""
lista = []
for i in napis:
    if i == " ":
        lista.append(temp)
        temp = ""
    
    temp = temp + i
    
lista.append(temp)
        

print(lista)
        
def sprawdzenie_hasla(haslo):
    # wymagania to: dlugosc 10, male/duze litery, co najmniej jeden !
    duza = False
    mala = False
    wykrzyknik = False
    if len(haslo) < 10:
        return False
    
    for i in napis:
        if i.isupper:
            duza = True
        else:
            mala = True
        
    if "!" in napis:
        wykrzyknik = True
    
    if duza & mala & wykrzyknik is True:
        return True
        
print(sprawdzenie_hasla("Dawa!juz"))
print(sprawdzenie_hasla("Dawa!juzAsz"))
        
liczby = [1,22,31,41,99,42,51,65]


for i in liczby:
    if i != 99:
        print(i)
    
        
i = 1        
while i <= len(liczby):
    if liczby[i] == 99:
        print(i)
        break
    i += 1
    
plik = open("teks.txt", "r")
print(plik.read(), end='')

with open("teks.txt", "r") as file:
    for line in file:
        print(line, end='')
        
print(plik.readlines())

jezyki = ["html", "css", "php", "javascript", "python"]
    
        
with open("teks.txt", "w") as file:
    for line in jezyki:
        print(line, file=file)
    
    
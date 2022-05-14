# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:37:22 2022

@author: Dawid Borawski
"""
import math as m
import numpy as np
import random as rm

miasta = ['olsztyn', 'gdansk', 'warszawa', 'radom', 'sosnowiec']


wynik = list(map(lambda s: s[:3], miasta))
#print(wynik)



def macierz():
    lista = []
    with open('australian.dat', 'r') as plik:
        for line in plik:
            lista.append(list(map(lambda x: float(x), line.split())))
    return lista


lista = macierz()      

#for i in range(5):
    #print(lista[i])      
    
#Metryka:
    # Jeżeli |A|-|B|== 0 to A i B to ten sam punkt
    # |AB|=|BA|
    # nierównosć trójkąta zachodzi

def metryka_euklidesowa(x,y):   
    suma = 0

    for i in range(max(len(x),len(y))-1):
        suma += (x[i]-y[i])**2    
        
    return m.sqrt(suma)
        
#print(metryka_euklidesowa(lista[0], lista[1]))
#print(metryka_euklidesowa(lista[0], lista[2]))
#print(metryka_euklidesowa(lista[0], lista[3]))

#print("0-5: ",metryka_euklidesowa(lista[0], lista[5]))
#print("0-10: ",metryka_euklidesowa(lista[0], lista[10]))
#print("0-20: ",metryka_euklidesowa(lista[0], lista[20]))



# DO DOMU
# Funkcja, która policzy odległosc kazdego obiektu do obiektu 0
# pogrupować wględem klasy decyzyjnej (ostatni atrybut) do słownika { klasa decyzyjna: lista wartosci}

def mierzymy(lista, x):
    grupy = dict()
    tupla = []
    for i in range(1, len(lista)):
        decyzyjna = lista[i][14]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(metryka_euklidesowa(x, lista[i]))
            tupla.append(tuple((decyzyjna,metryka_euklidesowa(x, lista[i]))))
        else:
            grupy[decyzyjna] = [metryka_euklidesowa(x, lista[i])]
            tupla.append(tuple((decyzyjna,metryka_euklidesowa(x, lista[i]))))
    
    return grupy, tupla


x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

slownik, tupla = mierzymy(lista,x)




#print(slownik)
#print(tupla)

grupy_1 = dict()

for i in range(len(tupla)):
    decyzyjna = tupla[i][0]
    if decyzyjna in grupy_1.keys():
        grupy_1[decyzyjna].append(tupla[i][1])
    else:
        grupy_1[decyzyjna] = [tupla[i][1]]
        
#print(grupy)
    
#grupy[0].sort()
#grupy[1].sort()

#print(grupy[0][:5])
#print(grupy[1][:5])

#print(sum(grupy[0][:5]))
#print(sum(grupy[1][:5]))


def suma_k(slownik, k):
    grupy = dict()
    for klucz in slownik.keys():
        slownik[klucz].sort()
    for klucz in slownik.keys():
        suma = 0
        for i in slownik[klucz][:k]:
            suma += i
        grupy[klucz] = suma
    
    return grupy

grupy = suma_k(grupy_1, 5)
#print(grupy)
#print(grupy[1])

############## DO DOMU 2 ################
# minimum odleglosci do klasy
def decyzja(slownik):
    klucze = list(slownik.keys())
    ilosc = 1
    klasa = klucze[0]
    minimum = slownik[klucze[0]]
    for key in klucze[1:]:
        if minimum > slownik[key]:
            minimum = slownik[key]
            klasa = key
            ilosc=1
        elif minimum == slownik[key]:
            ilosc+=1
    if ilosc > 1:
        return 
    return klasa

#print("Decyzja:",decyzja(grupy))

def metryka_euklidesowa_2(x,y):
    v1 = np.array(x)
    v2 = np.array(y) 
    a = v2 - v1
    a2 = np.dot(a,a)
    return m.sqrt(a2)
    
    
#print(metryka_euklidesowa_2(lista[0], lista[1]))
#print(metryka_euklidesowa_2(lista[0], lista[2]))
#print(metryka_euklidesowa_2(lista[0], lista[3]))

def losowa_wartosc_14(lista):
    for i in range(len(lista)):
        lista[i][-1] = rm.choice([0,1])
    return lista

lista_2 = losowa_wartosc_14(lista)
#print(lista_2)

def sortoowanie_przez_klucz(dane):
    posortowany_slownik = {}
    for i in dane:
        if i[14] not in posortowany_slownik.keys():
            posortowany_slownik[i[14]] = [i]
        else:
            posortowany_slownik[i[14]].append(i)
    return posortowany_slownik

def wyrodkowanie(posortowany_dane):
    slownik = {}
    for key in posortowany_dane.keys():
        temp = {}
        for x in range(len(posortowany_dane[key])):
                dist = 0
                for y in range(len(posortowany_dane[key])):
                    if x != y:
                        dist += metryka_euklidesowa_2(posortowany_dane[key][x], posortowany_dane[key][y])
                temp[tuple(posortowany_dane[key][x])] = dist
        slownik[key] = list(list(temp.keys())[list(temp.values()).index(min(temp.values()))])
    return slownik

def decyzja_2(punkt, wysrodkowane_miejsca):
    slownik = []
    temp = wysrodkowane_miejsca.copy()
    for key in wysrodkowane_miejsca.keys():
        temp[key] = metryka_euklidesowa_2(punkt, wysrodkowane_miejsca[key])
    #slownik = [x for x,y in temp.items() if y == min(temp.values())]
    for x,y in temp.items():
        if y == min(temp.values()):
            slownik.append(x)
    return slownik[0]

def segregacja(dane1, dane2):
    wymiana = 1
    while wymiana > 0:
        wymiana = 0
        posortowany_dane = sortoowanie_przez_klucz(dane1)
        wyrodkowanie_danych = wyrodkowanie(posortowany_dane)
        for x in range(len(dane1)):
            if decyzja_2(dane1[x], wyrodkowanie_danych) != dane1[x][14]:
                dane1[x][14] = decyzja_2(dane1[x], wyrodkowanie_danych)
                wymiana += 1
    return dane1


wymieszane_dane = losowa_wartosc_14(lista)
posortowane_dane = sortoowanie_przez_klucz(lista)
wyrodkowanie_danych = wyrodkowanie(posortowane_dane)
wynik = segregacja(wymieszane_dane, lista)
#print(wynik)
slownik, tupla = mierzymy(wynik, x)
#print(decyzja(slownik))

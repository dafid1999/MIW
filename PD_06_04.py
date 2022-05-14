# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:31:30 2022

@author: Dawid
"""

import math as m
import numpy as np

def macierz():
    lista = []
    with open('x.dat', 'r') as plik:
        for line in plik:
            lista.append(list(map(lambda x: float(x), line.split())))
    return lista


macierz = macierz()   

def srednia_arytmetyczna(lista):
    suma = 0.0
    for x in lista:
        suma += x
    return float(suma / float(len(lista)))
    
def wariancja(lista):
    srednia = srednia_arytmetyczna(lista)
    suma = 0.0
    for x in lista:
        suma += pow(x - srednia, 2)
    return float(suma / float(len(lista)))

def odchylenie_standardowe(lista):
    return m.sqrt(wariancja(lista))

lista = []    
for x in macierz:
    lista.append(x[:14])
    
#print(srednia_arytmetyczna(lista[0]))
#print(wariancja(lista[0]))
#print(odchylenie_standardowe(lista[0]))


def srednia_arytmetyczna_iloczyn_skalarny(lista):
    return float(np.dot(lista,[1 for x in lista])/len(lista))


#print(srednia_arytmetyczna_iloczyn_skalarny(lista[0]))
    
def wariancja_skalarnie(lista):
    srednia = srednia_arytmetyczna_iloczyn_skalarny(lista)
    lista = np.array(lista)
    x = np.ones(lista.shape)
    y = np.dot(srednia, x)
    a = lista - y
    aa = a
    
#wariancja_skalarnie(lista[0])

#xy = macierz()
#macierz = np.array(xy)
#print(macierz)

def srednia_aryt_macierz(lista):
    ones = np.ones((len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista),ones)[0]

def wariancja_macierz(lista):
    srednia = srednia_aryt_macierz(lista)
    ones = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - ones
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def odchylenie_std_macierz(lista):
    return m.sqrt(wariancja_macierz(lista))



#print(srednia_aryt_macierz(macierz[0]))
#print(wariancja_macierz(macierz[0]))
#print(odchylenie_std_macierz(macierz[0]))

def macierz_kowariancji(macierz):
    return np.dot(macierz.T,macierz)


def odwrotnosc_macierzy(macierz):
    return np.linalg.inv(macierz)

def lewa_odwrotnosc_macierzy(macierz):
    kowariancja = macierz_kowariancji(macierz)
    odwrotnosc = odwrotnosc_macierzy(kowariancja)
    return np.dot(odwrotnosc,macierz.T)

def regresja_liniowa(macierz):
    macierz_x = []
    for x in macierz:
        macierz_x.append([1,x[0]])
        
    macierz_y = []
    for x in macierz:
        macierz_y.append(x[1])

    macierz_x = np.array(macierz_x)
    macierz_y = np.array(macierz_y)
    lewa_odwrotnosc = lewa_odwrotnosc_macierzy(macierz_x)
    return np.dot(lewa_odwrotnosc,macierz_y)


# B = (xT*x)^-1*xT*y
# (2,1) (5,2) (7,3) (8,3)
# wyniki: [2/7, 5/14] - B

x_y=np.array([[2,1],[5,2],[7,3],[8,3]])
print("2/7 = ", 2/7, "5/14 = ", 5/14)
print(regresja_liniowa(x_y))

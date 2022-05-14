# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:57:21 2022

@author: Dawid
"""
# 28.02.2020 wyklad 1h 10 o metodzie
# dla siebie - pierwiastkowanie
# DO DOMU 
# Zasada całkowania monte carlo
# Całka - metoda prostokątów lub trapezów, parametr Epsilon - stopien precyzji
# lub ilosc podzialow

import math as m
import random as rm

def dzielenie(liczba, epsilon):
    a, b = liczba, 1
    while abs(a-b) > epsilon:
        a, b = (a+b)/2, liczba/((a+b)/2)
    return a

#print(dzielenie(4, 0.00000000000000000001))
#print(dzielenie(9, 0.000000001))
#print(dzielenie(16, 0.0000000000001))

def funkcja(x):
    return (x**4+ 3*x**2 + 1)/2
    #return x


def funkcjaW(x,y):
    if ((y > 0) & (y <= funkcja(x))):
        return 1
    elif((y > 0) & (y <= funkcja(x))):
        return -1
    return 0


def monte_carlo(foo, xp, xk, dokladnosc):
    yp = 0
    yk = m.ceil(max(foo(xp), foo(xk)))
    
    punktyW = 0
    for i in range(dokladnosc):
        punktyW += funkcjaW(rm.uniform(xp, xk), rm.uniform(yp, yk))
    return (punktyW / float(dokladnosc)) * (xk-xp) * (yk-yp)
            

#print(monte_carlo(funkcja, -5, 13, 100000))
print(monte_carlo(funkcja, 0, 1, 10000000))


def trapezy(funkcja, poczatek, koniec, liczba_trapezow):
  integral = 0
  dx = (koniec-poczatek)/liczba_trapezow
  for i in range(liczba_trapezow):
    fpoczatek = poczatek + dx * i
    fkoniec = poczatek + dx * (i + 1)
 
    integral += (funkcja(fpoczatek) + funkcja(fkoniec)) / 2 * dx
  return integral
 

print(trapezy(lambda x: (x**4+ 3*x**2 + 1)/2, 0.0, 1.0, 100))
print(trapezy(lambda x: x, 0.0, 1.0, 100))
    
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:32:44 2022

@author: Dawid
"""

import math as m
import numpy as np

float_formatter = "{:.4f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})

a=np.array([[2.,1.,3.],
            [1.,6.,7.],
            [3.,7.,9.],])
b=np.array([[1.,0],
            [1.,1.],
            [0.,1.],])
c = np.array([[0, 2], 
              [2, 0],
              [1,2]])


def QRdecomposition(macierz):
    lista_v, lista_u, Q = [],[],[]
    for i in range(len(macierz[1])):
        v = []
        for x in macierz:
            v.append(x[i])
        lista_v.append(v)
    
    for v in lista_v:
        v = np.array(v)
        proj = 0
        for u_x in lista_u:
            u_x = np.array(u_x)
            proj += (np.dot(v.T,u_x)/np.dot(u_x.T,u_x))*u_x
        u = v - proj
        lista_u.append(u)
        if m.sqrt(np.dot(u.T,u)) == 0:
            e_x = u
        else:
            e_x = (1/m.sqrt(np.dot(u.T,u)))*u
        Q.append(e_x)
    macierzQ = np.array(Q).T
    macierzR = np.dot(macierzQ.T,macierz)
    return macierzQ, macierzR

Q, R = QRdecomposition(a)
print('Q(a)', Q,'\nR(a)', R)

QQ, RR = QRdecomposition(b)
print('Q(b)', QQ,'\nR(b)', RR)

QQQ, RRR = QRdecomposition(c)
print('Q(c)', QQQ,'\nR(c)', RRR)

def wartosci_wlasne(macierz, powtorzenia):
    for i in range(powtorzenia):
        Q,R = QRdecomposition(macierz)
        macierz = np.dot(R, Q)
    return np.diag(macierz)

print("wartosci wlasne dla macierzy a: ",
      np.round(wartosci_wlasne(a, 50),decimals=3))



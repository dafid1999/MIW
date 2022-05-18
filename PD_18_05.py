# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:59:05 2022

@author: Dawid
"""

import numpy as np
import math as m


Baza = np.array([[1.,1.,1.,1.,1.,1.,1.,1.],
              [1.,1.,1.,1.,-1.,-1.,-1.,-1],
              [1.,1.,-1.,-1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,1.,1.,-1.,-1.],
              [1.,-1.,0.,0.,0.,0.,0.,0.],
              [0.,0.,1.,-1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,1.,-1.,0.,0.],
              [0.,0.,0.,0.,0.,0.,1.,-1.]])

ortogonalna = np.dot(Baza,Baza.T)
#print(ortogonalna)

Dlugosci = []

for x in Baza:
    temp = 0
    for y in x:
        temp += m.sqrt(y**2)
    Dlugosci.append(temp)
    
#print(Dlugosci)
#print(Dlugosci==np.diag(ortogonalna))

ortonormalna = []

for i in range(len(Baza[0])):
    ortonormalna.append(Baza[i]*(1/m.sqrt(Dlugosci[i])))

ortonormalna = np.array(ortonormalna)

jednostkowa = np.diag(np.ones(8))
Xa = np.array([8., 6., 2., 3., 4., 6., 6., 5.])
Xb = np.dot(ortonormalna.T, Xa)
print(Xb)
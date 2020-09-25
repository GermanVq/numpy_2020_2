# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:05:34 2020

@author: German
"""
import time
import numpy as np

size = 10000

# Listas en python
l1 = list(range(size))
l2 = list(range(size))

start = time.time()
l3 = []
for x in range(len(l1)):
    l3.append(l1[x]+l2[x])
print(l3)
print('Total segundos: ', (time.time()-start)*10000)

# Listas en numpy
n1 = np.arange(size)
n2 = np.arange(size)

start = time.time()
n3 = n1 + n2
print('Total segundos: ', (time.time()-start)*10000)

# METODOS  DE NUMPY

a = [2, 3, 4, 5, 6]
b = [7, 9, 10, 11, 12]
c = [[3, 4, 5], [5, 7, 8], [4, 6 ,7]]

n1 = np.array(a)
n2 = np.array(b)
n4 = np.array(c)

# Operaciones

n3 = n1 + n2
n3 = n1 - n2
n3 = n1 * n2
n3 = n1 / n2

# Dimensión de un vector

n3.shape()

# matriz de ceros

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
c = [[3, 4, 5], [5, 7, 8], [4, 6, 7]]

n1 = np.array(a)
n2 = np.array(b)
n3 = np.array(c)

# Operaciones

n3 = n1 + n2
n3 = n1 - n2
n3 = n1 * n2
n3 = n1 / n2

# Dimensión de un vector

n3.shape

# matriz de ceros

n4 = np.zeros((5, 5))

# matriz de unos

n4 = np.full((4, 5), 7)

# matriz identidad

n4 = np.eye(5)

# matriz con elementos random

n4 = np.random.random((3, 3))

# matriz inversa

np.linalg.inv(n4)

# Elemento mas grande de una matriz

n3.max()

# Elemento mas pequeño de una matriz

n3.min()

# Promedio de una matriz

n3.mean()

# Suma elementos de una matriz

n3.sum()

# Raiz cuadrada de los elementos de una matriz

np.sqrt(n3)

# Seno

np.sin(n3)

# Coseno

np.cos(n3)

# Validar elementos iguales

a = [[3, 4, 5], [5, 7, 8], [4, 6, 7]]
z = [[3, 4, 5], [5, 7, 8], [4, 6, 7]]

na = np.array(a)
ns = np.array(z)

na == ns



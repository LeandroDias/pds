# coding: utf-8
import numpy as np

a = np.random.random((2, 3))
print("a: \n", a, end='\n')
print("Soma de a:", a.sum())
print("Mínimo de a:", a.min())
print("Máimo de a:", a.max())

b = np.arange(12).reshape(3, 4)
print("\nb: \n", b, end='\n')
print("Soma de b:", b.sum())
print("Mínimo de b:", b.min())
print("Máximo de b:", b.max())

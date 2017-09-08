# Crie uma matriz 2D 10x10 com valores ‘0’ no centro e ‘1’ nas bordas.

import numpy as np

a = np.zeros((10, 10))

a[[0]] = 1
a[[9]] = 1
a.T[0] = 1
a.T[9] = 1

print(a)

import numpy as np

a = np.ones((2, 3))
print("a:\n", a, end='\n')

a *= 3
print("a:\n", a, end='\n')

b = np.random.random((2, 3))
b += a
print("b:\n", b, end='\n')

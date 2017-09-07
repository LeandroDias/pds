import numpy as np

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

C = A * B
print(C, end='\n')

C = A.dot(B)
print(C, end='\n')

print(np.dot(A, B))

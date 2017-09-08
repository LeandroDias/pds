# Crie um vetor randômico 5x5 e subtraia dele a média de suas colunas.

import numpy as np

a = np.random.random((5, 5))

for col in range(a.shape[1]):
    media = a.T[col].sum() / len(a.T[col])
    a.T[col] = a.T[col] - media

print(a)

# Crie um vetor de inteiros de tamanho 10 e converta-o para float.

import numpy as np

a = np.random.randint(10, size=10)
for item in a:
    item = float(item)
print(type(a))

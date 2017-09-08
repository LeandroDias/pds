# Normalize (max=1 e min=0) uma matriz randômica de tamanho 5x5.

import numpy as np

a = np.random.random((5, 5))

max_a = a.max()
min_a = a.min()

normalized_a = (a - min_a) / (max_a - min_a)
print(normalized_a)

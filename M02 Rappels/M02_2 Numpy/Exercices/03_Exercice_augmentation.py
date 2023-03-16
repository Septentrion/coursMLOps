import numpy as np

a = np.array([82, 92, 89, 65, 77, 66, 69, 65, 79, 51], dtype=np.float64)
rate = lambda x: x*1.1
# il génère un nouveau tableau fonction du calcul qu'il vient de faire et donc il change le type
a = np.where( a % 2 == 0, rate(a) , a)

print(a)

## Deuxième solution
a = np.array([82, 92, 89, 65, 77, 66, 69, 65, 79, 51], dtype=np.float64)
rate = lambda x: x*1.1
a[ a % 2 == 0] = rate(a[ a % 2 == 0])

print(a)
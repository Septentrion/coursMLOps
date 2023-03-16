
import numpy as np 

x1 = np.array([[9, 1, 2],
    [8, 0, 2],
    [5, 1, 5]])

# 1 première ligne
x1[0,:]

# 2 deuxième colonne
x1[:,0]

# 3 somme lignes et colonnes
print( x1.sum(1) ) # lignes
print( x1.sum(0) ) # colonnes

# 4 Destructuration somme des colonnes
(c1, c2, c3) = x1.sum(0)

# 5 Destructuration somme des lignes
(l1, l2, l3) = x1.sum(1)

# Dimension 2x2x2
x2 = np.array([ 
    [ [8, 4],[8, 9] ],
    [ [3, 0],[5, 0] ] 
])

# 6 somme axis = 0
print(x2.sum(0))

# 7 somme axis = 1
print(x2.sum(1))

# 8 somme axis = 2
print(x2.sum(2))

# 9 tableau de dimension 1X3 somme total de chaque ligne
x3 = x2.sum(2).sum(1)

# Sélection

x2[:, :, -1]

"""
array([[4, 9],
       [0, 0]])

"""
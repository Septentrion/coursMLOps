
import numpy as np

A = np.array([
    [13, 22, 28, 66, 40],
    [16, 59, 37, 33, 28],
    [34, 98, 54, 48, 96],
    [13, 84, 93, 79, 76],
    [63, 50, 10, 69, 12]
])

# optimal les gardez sous forme d'un générateur et d'itérer lorsqu'on a besoin de les afficher 
pos_min = zip(A .min(1), A .argmin(1))

for (min, pos) in pos_min:
    print(min, pos)

print( list( zip(A .min(1), A .argmin(1)) ) )

pos_min = np.array(list( zip(A .min(1), A .argmin(1)) ) )


"""
Recherche des étudiants 
"""

# Autre solution Théo
def minTabLine(l):
    return [(np.amin(a), np.argmin(a)) for a in l]

A = np.array([
    [13, 22, 28, 66, 40],
    [16, 59, 37, 33, 28],
    [34, 98, 54, 48, 96],
    [13, 84, 93, 79, 76],
    [63, 50, 10, 69, 12]
])

print(minTabLine(A))

# Dylan
minTabLine = [(int(np.where(row == np.amin(row))[0]), np.amin(row)) for row in A]
print(minTabLine)
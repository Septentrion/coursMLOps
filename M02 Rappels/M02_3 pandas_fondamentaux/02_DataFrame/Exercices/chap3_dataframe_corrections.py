import pandas as pd
import numpy as np

"""
Corrections des exercices Pandas DataFrame
"""

# Exercices manipulation des index & column

"""
Remplacez à l'aide de la méthode replace de Pandas remplacez 
les données manquantes ci-dessous par la valeur np.nan de Numpy :

"""

df = pd.DataFrame(
    [
        [1, "2", None, 3], 
        [4, None, "5", 6],
        [7, 8, 9, 10], 
        ["None", "", None, "NAN"],
    ],
    index=['a', 'b', 'c', 'd'],
    columns = ['A', 'B', 'C', 'D']
)

df.replace([None, "", "NAN"], [np.nan, np.nan, np.nan], inplace=True)

##

A = pd.Series(np.random.randint(1, 10, 15))
B = pd.DataFrame( A.values.reshape(3,5), index=list("abc"), columns=list("defgh") )


## Exercice somme et remplacement

"""
1. Faites la somme de toutes les valeurs négatives de C

2. Remplacez dans la colonne b les valeurs négatives par 
la moyenne des valeurs positives de la colonne.

"""

C = pd.DataFrame( np.random.randn(5, 5), columns=list("abcde"), index=list("fghij")) 

# Accèder à la colonne b 
C['b']

# Remplacez les valeurs négative par la moyenne des valeurs positives de la 
# colonne
C['b'][C['b'] < 0] = C['b'][C['b'] > 0].mean()


## Exercice Matrice et recherche

data = [ 
    [13,  54,  23,  23,  62,  29,  53,  15,  54 , 67],
    [13,  54,  23,  23,  62,  29,  53,  15,  54,  67],
    [98,  36,  34,  40,  13,  92,  41,  61 , 94,  62],
    [33,  87,  46,  44,  82,  87,  11,  76,  76,  21],
    [56,  16 , 13,  91,  64,  13,  77,  44,  44,  27],
    [15 , 87,  20,  50,  53,  48,  39,  38,  91,  32],
    [93,  48,  28,  27,  50 , 55 , 28 , 38  ,78 , 85],
    [76,  58 , 26  ,89 , 88  ,71 , 97 , 80,  42,  52],
    [38,  98,  55,  61,  75,  82 , 37,  64,  87,  83],
    [24,  53,  16,  84,  82,  13,  18,  18,  82,  51],
  ]

A = pd.DataFrame(data, index=list("abcdefghij"), columns=list("abcdefghij".upper()))
print(A)

lines = A[A.duplicated()].index.values

for line in lines:
    A.drop(line)

# comptage

columns = [ "A",   "B",   "C",   "D",   "E",   "F",   "G",   "H",   "I",   "J"]

stat = {}

for index, row in A.iterrows():
    for c in columns:
        stat[row[c]] = A[A == row[c]].count().sum()
        
        
print(A[A == 13].count().sum())

print(stat)

# Somme des lignes

B = A[ A.apply(lambda x : x % 2 == 0) ].sum()

## Exercice dimension et génération

A = pd.DataFrame( np.arange(1, 10) * np.arange(1, 10).reshape(9,1),
                 index=list("abcdefghi"), 
                 columns=list("abcdefghi".upper()) )
# Moyenne 

A.mean(axis = 0)
A.mean(axis = 1)

# 2. Ajoutez la matrice B à l'unique colonne de la matrice A possible. Puis faites la somme en ligne, puis en colonne en utilisant la transposition.
B = pd.DataFrame([11, 6, 4, 8, 0, 9, 7, 8, 13], index=list("abcdefghi"), columns=['A'])
A['A'] =  B + A

print(A.sum())
print(A.T.sum() )
print(A)

# pourcentage par ligne et colonne

# par ligne
print( 'ligne', (A.T / A.T.sum()).T )

# colonne
print('colonne', A/A.sum())
import pandas as pd

import numpy as np

dataset = {
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'city':['Paris','Lille','Paris','Lille',
    'Paris','Bordeaux','Bordeaux'],
    'num_children':[3,0,2,4,3,1,5],
    'num_pet':[5,1,0,5,2,2,3],
    'status' : [
        'married', 
        'married', 
        'married', 
        'divorced', 
        'divorced', 
        'married', 
        'married']
}

df = pd.DataFrame(dataset)
dfG = df.groupby('city')['city', 'num_children'].sum()
dfG.head()

# Ecart des ages par ville

# Series
print( df.groupby('city')['age'].apply(lambda x : x.max() - x.min()) )

# DataFrame
print( df.groupby('city')[['age']].apply(lambda x : x.max() - x.min()) )


# 3. Est-ce que les femmes mariées ont plus d'enfant que les hommes divorcés ?

dfF = df[ (df['status'] == 'married') & (df['gender'] == 'F' ) ]['num_children'].sum()
dfM = df[ (df['status'] == 'married') & (df['gender'] == 'M' ) ]['num_children'].sum()

print(dfF.index)

print(type(dfM))

# par les index de la série ici gender
print(dfF['F']  > dfM['M'])

# 4. Quelle est la ville ou les femmes ont le plus de chien ? Même question pour les hommes ?
numPetF = df[ df['gender'] == 'F' ].groupby('city')['num_pet'].sum().idxmax()

print(numPetF)

numPetM = df[ df['gender'] == 'M' ].groupby('city')['num_pet'].sum().idxmax()

print(numPetM)

## Exercice pourboire
tips = pd.read_csv('data/tips.csv')

"""
1. Ajoutez une colonne **tips_perct** au DataFrame tips, 
elle calculera le pourcentage de chaque pourboire par 
rapport au total des pourboires.
"""

tips['tips_perct'] = tips['tip'] / tips['total_bill']

"""
2. Quelles sont les pourcentages des pourboires par rapport 
au sex et à la consommation de tabac ? Donnez leurs moyennes 
et écarts types.

"""

tips.groupby(['sex', 'smoker'])['tips_perct'].agg(['mean', 'std'])

def peak_to_peak(arr):
    
    return arr.max() - arr.min()

"""

3. Calculez l'étendue des pourboires pour les femmes 
qu'elles fument ou ne fument pas. Créez une fonction 
peak_to_peak et appliquez cette fonction, comme une 
fonction d'agrégation, à votre groupement à l'aide de 
la fonction agg de Pandas.

"""

tips.groupby('smoker')['tip'].agg(peak_to_peak)


"""
 4. En utilisant le même regroupement par sex et smoker 
et en utilisant la fonction agg de Pandas, calculez le max 
des pourboires ainsi que le nombre. Vous pouvez passer 
à la méthode agg un dictionnaire pour spécifier les fonctions 
à appliquer par colonne.
"""

tips.groupby(['sex', 'smoker']).agg({'tip' : np.max, 'size' : np.sum})

## Exercice grouper avec un dictionnaire

"""
Soit le DataFrame population ci-dessous. On supposera qu'il

"""

population = pd.DataFrame(np.random.randn(5, 5), 
                          columns=list("abcde"),
                          index=["Alan", "Bernard", "Sophie", "Noe", "Alice"] )
print(population)
mapping = {'a' : 'first', 'b' : 'first', 'c': 'second', 'd' : 'second', 'e' : 'second'}

grouped = population.groupby(mapping, axis=1).sum()
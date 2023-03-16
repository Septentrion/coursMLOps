#  TP 04

## Partie 1 Iris obligatoire

Récupérez les sources du datasets dans le module sklearn

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

print(iris.keys())
```

1. Donnez le nombre de catégorie de fleurs ainsi que leurs noms respectifs.

2. Comptez le nombre de fleurs par catégorie.

3. Calculez la moyenne des longueurs des pétales, puis des sépales de toutes les fleures. Puis, refaite ce calcul par catégorie de fleurs.

4. Trouvez la fleur qui a la plus longue (en longueur) pétale, puis la plus grande surface (longueur x largeur).

Pour la suite utilisez la méthode plt.hist de Matplotlib.

5. Faites l'histogramme des longueurs des pétales des versicolors.

6. Faites l'histogramme des longueurs des pétales des setosas.

7. Faites l'histogramme des longueurs des pétales des virginica.

## Partie 2 facultative

1. Créez une fonction de Bernoulli, elle a deux issues possibles : 1 ou 0. Passez en paramètre la probablité p d'obternir 1 à cette fonction.

```python
def bernouilli(p):
    pass
```

- Problématique :

Si on prend l'expérience suivante : on lance successivement 10 fois une pièce de monnaie parfaitement équilibrée. Quelle est la probabilité d'obtenir 3 piles sur ces 10 lancers ?

2. Créez une fonction **experience(n,p)** qui permet de simuler un lancer de pièce à l'aide de la fonction bernoulli.

3. Répétez un grand nombre de fois l'expérience décrite ci-dessus et comptez alors le nombre de fois que l'on obtient une combinaison de 3 piles parmi 10 lancers :

```python
experience(n,p) == 3
```

# Modules

Python possède une centaine de Modules standards. D'autres modules (nombreux) tiers existent également que l'on peut importer dans nos projets.

[liste des modules standards](https://docs.python.org/3/py-modindex.html)

## Introduction

Un module est un fichier Python, lorsqu'on importe ce fichier cela crée un objet Module.

Un module contient un certains nombres de fonctions similaires.

```python
import random

# C'est un objet de type Module
print(random)

# accéder à l'ensemble de ses attributs
dir(random)

# demander de l'aide
help(random)
```

Notez que help est plutôt utilisé pour demander de l'aide sur une méthode d'un module.

```python
# Dans Ipython sinon help(random.randint)
random.randint?
```

## Import de modules

Recommandation pour les imports de module dans Python :

1. On importe les imports de la librairie standard de Python en premier.

2. On importe tous les modules tout en haut d'un script Python.

3. On importe par bloque des modules semblables

4. On importe les modules de l'application en dernier

Un module est un fichier Python, donc si vous mettez du code qui s'exécute dans ce fichier et que vous l'importer alors il s'exécutera également dans le fichier qui importe ce module. Il faut donc créer des fonctions ou classes dans les fichiers importés.

Dans l'import suivant vous importez le module utils, pour accéder aux fonctions de ce module vous utiliserez la syntaxe suivante

```python
import utils

utils.mult([1,2,3], [1,2,3])
```

Vous pouvez si vous le souhaitez importer qu'une seule fonction de ce module, vous pouvez également créer un alias de nom pour la fonction importée :

```python
from utils import mult as m

m([1,2,3], [1,2,3])
```

## Package

Un ensemble de modules peut être regrouper dans un package.

Supposons que l'on est le package Core avec le module utils à l'intérieur alors pour importer le module utils on fera :

```python
import Core.utils
```

## Scripts

Vous pouvez également vouloir exécuter un fichier en tant que script dans ce cas vous écrirez dans le fichier le code suivant :

```python

def square (a):
    return a**2

if __name__ == "__main__":
    print( square(2) )
```

Dans le cas où vous exécutez ce fichier en ligne de commande :

```bash
python square.py
# 4
```

Et dans le cas où vous importez ce fichier en tant que module, dans ce cas il n'y aura pas d'exécuter du script dans la partie conditionnelle et vous pourrez utiliser les fonctions du module classiquement.

```python
import square as s

print(s.square(10))
```

## Package plus complexe

Vous pouvez également avoir une structure plus complexe de modules, supposons que l'on ait la structure de modules suivantes :

```text
Algo/
    calculator/
        addition.py
    arithmetic/
        fibo.py
app.py
```

Ainsi dans le script app.py vous pourrez importer les fonctions du module arithmetic comme suit 

```python
from Algo import fibo as f
f.fib(10)
```

# TP

Récupérez le dataset dans le dossier Data : "pollution_2016.csv".

1. Importez les données dans votre script Python et enregistrez les dans un array numpy. Travaillez avec un type composite.

2. Affichez le nom du pays et le pourcentage du pays qui a le plus fort taux de pollution.

3. Calculez la moyenne des taux de pollution, l'écart type et l'étendu (voir les indications).

4. Classez les pays par taux de pollution croissant et décroissant.

5. Affichez les 5 plus gros pollueurs.

6. Une augmentation globale de 0.01% de la pollution a eu lieu en 2017 par rapport à 2016. Créez un nouveau fichier pollution_2017.csv


Indications :

```python
import numpy as np
import csv
import pprint

A = np.array([1, 2, 3])

# écart type
np.std(A)

with open('../Data/pollution_2016.csv','r') as f:
    data_reader = csv.reader(f, delimiter = ',', quotechar = '"')
```

L'étendu c'est la différence entre le max et le min des valeurs de la série statistique.

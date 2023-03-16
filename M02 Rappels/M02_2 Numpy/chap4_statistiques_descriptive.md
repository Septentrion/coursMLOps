# Descriptive généralites

Une variable statistique est dite :

## Quantitative

- **quantitative** : lorsqu'elle est mesurée par un nombre (les Notes des Etudiants à l'Examen de Statistique, le Chiffre d'Affaire par PME, le Nombre d'Enfants par Ménage, . . . ).

On distingue 2 types de variables quantitatives :

- les variables quantitatives discrètes
- Les variables quantitatives continues.

Par exemple le nombre d'enfants par ménage ne peut être que 0, ou 1, ou 2, ou 3, . . .C'est une variable quantitative discrète.

Les variables **quantitatives continues** peuvent prendre toute valeur dans un intervalle. Par exemple, le chiffre d'affaire par PME, le temps d'attente à un arrêt de bus.

## Qualitative

Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des noms. Par exemples, les modalités d'une variable Sexe peuvent être : Masculin et Féminin.

On distingue deux types de variables qualitatives : les variables qualitatives ordinales et les variables qualitatives nominales.

Plus précisément une variable qualitative est dite **ordinale**, lorsque ses modalités peuvent être classées dans un certain ordre naturel (c'est par exemple le cas d'une variable commen Mention au Bac).

Une variable qualitative est dite **nominale**, lorsque ses modalités ne peuvent être classées de façon naturelle (c'est par exemple le cas d'une variable comme Couleur des Yeux ou encore de la variable Sexe).

## Indicateurs de dispersion

On dispose d'une population de N individus, et on observe $x_1 , . . . , x_N$, les valeurs d'une variable quantitative discrète X pour ces individus.

### Définition de l'étendue

L'étendue de la variable X quantitative discrète est la différence entre la plus grande et la plus petite des valeurs observées.

$e = max(X_i) - min(X_i)$ où i décrit l'ensemble des valeurs de la variable X.

### Variance et écart type

La variance de la variable quantitative X, notée par Var(X), est, par définition, la moyenne arithmétique des carrés des écarts à la moyenne arithmétique.

$Var(X)=\frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^2$, $\bar{X}$ représente la moyenne.

Quand la série prend les valeurs $x_1, x_2, ..., x_k$ avec les fréquences $f_1, f_2, ..., f_k$, sa variance est :

$Var(X)=\sum_{i=1}^{k}f_i \times(X_i - \bar{X})^2$

## 01 Exercice calcul de la variance

1. Soit la série statistique suivante :

```python
Notes = [7, 9, 11, 12, 13, 15]
```

Ecrire un script en Python qui permet de calculer la variance de cette série. Pensez à utiliser numpy.

2. Soit le tableau de notes d'une classe suivant :

| Note             |     Effectif             |
| -------------    |  ----------------------: |
| 7                |        5                 |
| 9                |        4                 |
| 11               |        21                |
| 12               |        35                |
| 13               |        32                |
| 15               |        3                 |

2.1 Calculez la moyenne des notes de cette classe.

2.2 Déterminez la médiane. Faites un script en Python.

2.3 Déterminez la variance. Utilisez le code précédent en Python pour calculer la variance.

2.4 On définit l'écart type comme étant la racine de la variance. Calculez l'écart type des notes de cette classe.

3. L'enseignant augment toutes les notes de 1 point. Quelle conséquence cela a pour les calculs précédents ?


## 02 Exercice fréquence

Récupérez le dataset dans student.csv, dans le dossier data et étudiez le critère couleur des yeux.

1. Récupérez les données du dataset dans un fichier Python ou Notebook.

2. Edutiez le critère "Couleur des yeux" et calculez la fréquence d'apparition de ce critère.

3. Créez à partir du tableau précédent un diagramme en secteur pour visualiser la répartition de la couleur des yeux.

## 03 Exercice notes en statistique

Récupérez le dataset **note_statistiques.csv** et faite un diagramme en baton des notes en statistiques.

1. Calculez les fréquences des notes. Ajoutez un argument à votre tableau numpy.

2. Faites maintenant des classes de valeurs de largeur 4 pour les notes, ajoutez un argument Notes_bin dans votre tableau.

4. Créez à partir de un nouveau tableau un diagramme en baton regroupant les notes dans par classe, utilisez un dictionnaire. 

La classe modale est la classe dont la fréquence par unité d'amplitude est la plus élevée.

Cette classe correspond donc au rectangle le plus haut de l'histogramme des fréquences.

Trouvez la classe modale de notre dataset notes statistiques.


## Médiane et Quantile

Ces objets sont des **indicateurs de position** en statistiques. Au même titre que la moyenne.

La médiane (notée Me ) d'une variable quantitative est la valeur de cette variable qui permet de scinder la population étudiée en deux sous-populations de même effectif.

La notion de quantile d'ordre $\alpha$ ($0 \leq \alpha \leq 1$), encore appelée fractile d'ordre $\alpha$, généralise la notion de médiane. Le quantile d'ordre $\alpha$ d'une variable quantitative X, est la valeur $X_{\alpha}$ de cette variable qui permet de scinder la population étudiée en deux sous-populations dont les effectifs respectifs sont égaux à $\alpha$ et 1 − $\alpha$ de l'effectif de la population initiale.

$Q_1 = x_{0,25}$ , s’appelle le premier quartile; un quart des valeurs prises par X sont inférieures ou égales à $Q_1$ . $Q_2$ = $x_{0,5}= Me$ est la médiane. $Q_3$ = $x_{0,75}$ s'appelle le troisième quartile; un quart des valeurs prises par X sont supérieures ou égales à $Q_3$.

## Définition de l'intervalle interquartile

C'est la différence entre le troisième quartile et le premier
quartile ; il s’écrit : $II = Q_3 - Q_1$.


## 05 Exercice Quartile notes

 Soit la série suivantes : 10; 25; 30; 40; 41; 42; 50; 55; 70; 101; 110; 111

 1. Déterminez le troisième quartile.

 2. La médiane.

 3. L'intervalle interquartile.

Même exercice avec la série statistique suivante, répondez aux 3 questions :

Soit la série suivantes : 10; 25; 30; 40; 41; 42; 50; 55; 70; 101; 110; 111, 208

## Diagramme en moustache

La boîte à moustaches résume quelques **indicateurs de position** d'un caractère étudié (médiane, quartiles, minimum, maximum ou déciles).

Une boîte à moustache aide à se représenter les données. Notons que 50% des valeurs sont à l'intérieur de la boîte. De même 50% des valeurs sont positionnées sur les moustaches, en deux intervalles de 25%. De plus lorsqu'on réalise un diagramme à moustache, on voit directement les valeurs extrêmes.

Ce diagramme est utilisé **principalement** pour comparer un même caractère dans deux populations de tailles différentes.

![diagramme moustache](images/box_plot.png)

Notez que les valeurs extèmes n'apportent en elle-même pas d'information particulière pour l'étude d'un critère.

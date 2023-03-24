import numpy as np
import pandas as pd
import tensorflow as tf
from keras import layers, models
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.optimizers import Adam

# -- 1 ---------------------------------------------------
# Lecture des données
df = pd.read_csv(dataFile)
df.head()
# --------------------------------------------------------

# -- 2 ---------------------------------------------------
# Préparation des données
# --------------------------------------------------------

# Mélanger les données
irisData = irisData.sample(frac=1)

# Séparer les entrées des sorties
labels = irisData[['label']]
features = irisData[['x1', 'x2', 'x3', 'x4']]
# Syntaxe alternative de sélection dans le DataFrame
# y = df.iloc[:,4].values
# X = df.iloc[:,0:4].values

# Séparer le jeu d'apprentissage du jeu de test

# A) Jeu d'apprentissage
train_X = features[0:135]
# Encodage oneHot des étiquettes
# Transformation des chaînes de caratères en vecteurs numériques
train_y = pd.get_dummies(labels[0:135])
# Autres syntaxes possibles
# 1. Avec Scikit-Learn et Keras
# train_y = y = to_categorical(LabelEncoder().fit_transform(labels))

# B) Jeu de test
test_X = features[135:]
test_y = pd.get_dummies(labels[135:])

print("Forme des caractéristiques d'entraînement :", train_X.shape)
print("Forme des étiquettes d'entraînement :", test_y.shape)
print("Forme des caractéristiques de test :", test_X.shape)
print("Forme des des étiquettes de test :", test_y.shape)

# Une autre manière de découper les données avec Scikit-Learn
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# -- 3 ---------------------------------------------------
# Construction du modèle
# --------------------------------------------------------

# Nous utilisons ici deux types de couches Keras :
# 1. Input, qui sert seulement à indiquer la taille du vecteur de données en entrée (ici 4)
# 2. Dense, qui indique une couche dont tous les neurones sont connectés aux précédents et aux suivants
# NB. Il n'y a pas de couche de sortie explicite, la dernière remplit cet office
model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(4,)))
# Chaque couche est associée à une fonction d'activation qui joue un peu le rôle « d'interrupteur »
# La fonction ReLu, par exemple, rend x si x > 0 et 0 si x < 0
# Ces fonctions sont essentielles au bon fonctionnement du système
# `relu` est la fonction principalement utilisée, avec `sigmoid`
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
# La fonction `softmax` est la principale fonction d'activation utilisée sur les couches de sortie pour les tâches de classification
# Son rôle est de faire en sorte que la somme de probabiités des différentes classes soit égale à 1
# et de mieux discriminer les différents résultats
model.add(tf.keras.layers.Dense(3, activation='softmax'))
model.summary()

"""
Autre syntaxe possible :
model = tf.keras.Sequential(
    layers = [
    tf.keras.layers.Input(shhape=(4,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
    ]
)

Ou encore sous forme fonctionnelle :
inputs = tf.keras.Input(shape=(4,))
x = layers.Dense(64, activation="relu")(inputs)
x = layers.Dense(64, activation="relu")(x)
outputs = layers.Dense(3, activation='softmax')(x)
model = keras.Model(inputs=inputs, outputs=outputs, name="iris_model")
"""

# Compilation du modèle
# L'optimiseur accélère la convergence du modèle vers la solution
# La fonction de perte (loss) est un estimateur de la qualité de l'apprentissage ('categorical_crossentropy' est le standard pourla classification)
# Les métriques permettentégalement d'évaluer la qualité du modèle
model.compile(optimizer=Adam(learning_rate=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# -- 4 ---------------------------------------------------
# Entraînement du modèle
# --------------------------------------------------------

# epochs : nombre d'itérations d'apprentissage
# batch_size : taille de lots interne à chaque itération
history = model.fit(train_X, train_y, epochs=1000, batch_size=16)
# Affichage de la courbe d'apprenissage
pd.DataFrame(history.history).plot()

# -- 5 ---------------------------------------------------
# Evaluation du modèle
# -------------------------------------------------------

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
# Valeur dinale de l'erreur (normalement autour de 0.1 - 0.2)
print('Test loss:', loss)
# Valeur finale de la précision (normalement au-dessus de 90%)
print('Test accuracy:', accuracy)

# -- 6 ---------------------------------------------------
# Utilisation du réseau
# --------------------------------------------------------

# Réalisation de prédictions avec l'ensemble de test
# `predict` soumet un ensemble d'exemples au modèle et rend le résultat sous forme de tableau
y_pred = model.predict(X_test)

# On peut vérfier que les résultats sont en fait des probabilités en affichant `y_pred`
# La probabilité la plus grande (en princie beaucoup plus élevée que les autres) est considérée comme la « réponse » ud système.
print(y_pred)

# Vérification de la pertinence des prédictions
# (`argmax` retourne l'indice de la valeur maximale d'un tableau)
actual = np.argmax(y_test,axis=1)
predicted = np.argmax(y_pred,axis=1)
print(f"Actual: {actual}")
print(f"Predicted: {predicted}")


import numpy as np
import csv
import pprint
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)  

# 1
with open('../../Data/students.csv', 'r') as f:
    data_reader = csv.reader(f, delimiter=',',quotechar='"')
    # Récupérer les données dans un tuple
    data = [(d[0], d[1], d[2], d[3], d[4]) for d in data_reader][1:]

data = np.array(data, dtype=np.dtype([
    ('Name', np.dtype('U16')),
    ('Color', np.dtype('U4')),
    ('Sex', np.dtype('U4')),
    ('Mention', np.dtype('U4')),
    ('Note', np.dtype('f8')),
]))

total = data.size

# 2
colors = np.unique( data['Color'] )
nbColors = colors.size
# création d'un tableau vide de valeurs
frequences = np.empty(nbColors, dtype=np.dtype('f8'))

# une lambda pour calculer les fréquences
fColor = lambda color : round (  (data['Color'] == color ).sum() / total, 2 )

for i, c in enumerate(colors):
    frequences[i] = fColor(c)

plt.figure(figsize=(12,8))

plt.pie(frequences, (0.05, 0.05, 0.05, 0.05), labels=colors, colors=['lightskyblue', 'brown', 'grey', 'green'], 
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.title("fréquences des couleurs des yeux")
plt.show()
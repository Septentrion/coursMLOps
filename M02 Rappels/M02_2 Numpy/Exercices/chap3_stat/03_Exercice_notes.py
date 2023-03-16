
import numpy as np
import csv
import matplotlib.pyplot as plt
import pprint
pp = pprint.PrettyPrinter(indent=4)  


with open('../Data/notes_statistiques.csv', 'r') as f:
    data_reader = csv.reader(f, delimiter=',', quotechar='"')
    data = [(d[0], d[1], np.nan, np.nan)
            for d in data_reader if d[0] != '0'][1:]

data = np.array(data, dtype=np.dtype([
    ('Notes', np.dtype('f8')),
    ('Effectif', np.dtype('f8')),
    ('Frequence', np.dtype('f4')),
    ('Notes_bin', np.dtype(
        [('min', np.dtype('f8')), ('max', np.dtype('f8'))])),
]))

total = data.size
m = int(np.max(data['Notes']))
print(data)


fig = plt.figure()

width = 0.5

plt.bar(data['Notes'], data['Effectif'], width, color='b')

plt.show()

group = {}
for i in range(0, 20, 4):           
    mask = (data['Notes'] >= i) & (data['Notes'] < i + 4.)
    group[f'{i}-{i+4}'] = mask.sum()

    data['Notes_bin'][mask] = (i, i + 4.)
    
print(group.keys())

fig = plt.figure()

width = 0.5

plt.bar( group.keys(), group.values(), width, color='b' )

plt.show()
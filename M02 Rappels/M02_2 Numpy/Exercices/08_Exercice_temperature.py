import numpy as np 

january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5, 7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2])

# 1 températures supérieures à 0
january[january > 0]

# 2 Comparez les températures 
# (january > 0).sum() > (january < 0).sum()
print( "Il y avait plus de températures positives que négative" if (january > 0).sum() > (january < 0).sum() \
      else  "Il y avait plus de températures négatives que positives" )

# 3 Pourcentage des températures > 0 sur le mois de Janvier
print( round ( (january > 0).sum() / len(january), 4 ) * 100 )

# 4  Créez un tableau days pour les jours du mois et donnez les jours pour lesquels 
# la température était supérieure à 0.
days_january = np.arange(1 , january.size + 1, dtype=np.int8)

days_january[january > 0]

# 5 Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.
january[9:][january[9:] > 0]

# 6 Les températures positivies et on va calculer leur moyenne
avg = np.mean(january[ january > 0 ])
january[ january < 0 ] = avg

print(january)
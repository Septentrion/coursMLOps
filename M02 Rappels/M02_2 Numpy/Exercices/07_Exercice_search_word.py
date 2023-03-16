from io import StringIO

import numpy as np

data = StringIO(u"""
6, 3, 3, 7, 7, 4, 7, 8, 5, 3, 7, 8, 4, 2
6, 9, 1, 2, 3, 4, 3, 1, 4, 3, 9, 6, 2, 2
a, a, a, a, a, a, a, a, a, a, a, a, a, a
4, 9, 2, 1, 1, 2, 3, 4, 3, 1, 9, 8, 2, 6
3, 2, 9, 9, 2, 3, 6, 9, 8, 2, 1, 2, 3, 4
1, 4, 1, 2, 3, 4, 4, 5, 8, 8, 1, 5, 7, 1
1, 4, 3, 8, 2, 1, 2, 3, 4, 3, 9, 3, 5, 8
7, 8, 8, 5, 1, 8, 3, 3, 6, 1, 2, 3, 4, 7
a, a, a, a, a, a, a, a, a, a, a, a, a, a
7, 7, 1, 6, 1, 2, 3, 4, 9, 2, 4, 4, 5, 9
5, 6, 6, 2, 3, 7, 1, 9, 9, 5, 1, 2, 3, 4
7, 7, 2, 3, 3, 7, 9, 4, 3, 9, 1, 1, 1, 1
6, 1, 2, 3, 4, 5, 5, 3, 1, 3, 1, 2, 3, 4
""")

dataNumbers = np.array(
    np.genfromtxt(data, delimiter=',', dtype=np.int8)
)

w = [1, 2, 3, 4]
def search_word(line):
    # 6, 1, 2, 3, 4, 5, 5, 3, 1, 3, 1, 2, 3, 4
    # 14 - 4 + 1 = 10 + 1 = 11 range(11) 0 10
    for i in range(1 + len(line) - len(w)):
        j = 0
        while j < len(w) and line[i+j] == w[j]:
            j+=1
        if len(w) == j:
            return i 

    return None

line = [6, 9, 1, 2, 3, 4, 3, 1, 4, 3, 9, 6, 2, 2]

print(search_word(line))
print(np.apply_along_axis(search_word, 1, dataNumbers))

# Méthode Mickael

def search_word(line):
    for i in range(1+len(line) - len(w)):
        word = line[i:i+len(w)]
        j = 0
        for k, ch in enumerate(word):
            if ch == w[k]:
                j += 1

        if j == len(word):
            return i

    return None

line = [6, 9, 1, 2, 3, 4, 3, 1, 4, 3, 9, 6, 2, 2]

print(search_word(line))
print(np.apply_along_axis(search_word, 1, dataNumbers))
r = [[1, 2], [3, 4], [5, 6]]

# copy de r
m = []
for e in r:
    m.append(e[:]) # faire une copy de chaque liste dans la nouvelle liste
    
# print(m)

m[0][0] = 100

print(r)
print(m)

# compréhension de liste pour faire une copie profonde de r

n = [ e[:] for e in r ]
n[0][0] = 100

print(r)
print(n)
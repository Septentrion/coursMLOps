
# on peut faire son propre générateur ou utiliser la fonction zip de Python
def myZip(l, m):
    assert len(l) == len(m)
    i = 0
    while i < len(l):
        yield (l[i], m[i])
        i += 1

l = [1, 2]
m = [10, 20]

# version pythonique de la somme
print(sum(a * b for a, b in myZip(l, m)))

z = myZip(l, m)
print(next(z))
print(next(z))

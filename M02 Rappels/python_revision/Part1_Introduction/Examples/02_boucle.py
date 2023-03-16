for x in range(1, 10):
	print(x)
 
# Objet itérable 
# les données sont non stockées il faut itérer sur cette objet pour afficher les données
print(range(1, 10))

print(list( range(1, 10)) )

def gen():
    i = 0
    while i < 100:
        yield i + 1
        i = i + 1


print(gen())

for i in gen():
    print(i)
    

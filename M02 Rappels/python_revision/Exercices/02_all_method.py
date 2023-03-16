
l = ['A', 'B', 'c']

# Ternaire avec compréhension de liste
print( 'Ok' if all (e.isupper() for e in l) else 'No' )
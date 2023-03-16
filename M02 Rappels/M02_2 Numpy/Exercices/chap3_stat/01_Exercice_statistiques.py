
import numpy  as np

# 1 variance
notes = np.array( [7, 9, 11, 12, 13, 15] )

avg = np.mean(notes)
print(avg)

v = np.sum( (notes - avg)**2 ) / len(notes)

print(v)

# 2 
note_students = np.array([(7,5),(9,4), (11,21), (12, 35), (13, 32), (15, 3)], dtype=[
     ('note', np.dtype('f8')),
    ('effectif', np.dtype('i8'))
])

avg_students = np.sum( note_students['note'] * note_students['effectif'] ) / note_students['effectif'].sum()

# 3
# // <=> division entière en Python
def my_mediane(numbers):
    i = len(numbers)//2
    
    if len(numbers) % 2 == 1:
        return numbers[i]
    
    return (numbers[i] + numbers[i + 1]) / 2.

effectifs = list(note_students['effectif'])
numbers = np.array( [ note_students['note'][i]  for i, k in enumerate( note_students['effectif']) for n in range(k)])

my_mediane(numbers)

# 4 variance
x = np.mean(numbers)
v = np.sum( (numbers - x)**2 ) / len(numbers)
print(v)

# Ecart type 

std = np.std(numbers)
print(std)
print(np.sqrt(v))

# on ajoute + 1
numbers = numbers + 1

# Cela ne change pas la manière dont les valeurs sont dispersées les unes par rapport aux autres
x = np.mean(numbers)
v = np.sum( (numbers - x)**2 ) / len(numbers)
print(v)

# Ecart type 

std = np.std(numbers)
print(std)
print(np.sqrt(v))
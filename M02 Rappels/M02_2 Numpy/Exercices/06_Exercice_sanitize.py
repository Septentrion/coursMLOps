students = np.array([
    [  "Name: Luce du Coulon" , "phone: 201-20-30"],
    [  "Name: Auguste Dupont", "phone: 201-22-30"],
    [  "Name: Roger Le Voisi", "phone: 201-27-30"],
    [  "Name: Alexandre Lacri", "phone: 201-10-30"],
    [  "Name: Jacques Humber", "phone: 201-20-35"],
    [  "Name: Thérèse Guille", "phone: 201-20-38"],
    [  "Name: Gilles Gros-Bodin", "phone: 201-20-39"],
    [  "Name: Amélie Pires", "phone: 201-25-39"],
    [  "Name: Marcel Laporte", "phone: 201-20-39"],
    [  "Name: Geneviève Marchal", "phone: 301-20-39"]
])

# 1
sanitize = lambda A, occ1, occ2 : [[ line[0][len(occ1):].strip(), line[1][len(occ2):].strip() ] for line in A ]

students_sanitize = sanitize(students, 'Name:', 'phone:')


# 2
mask = ["30" in el[1].split("-") for el in students_sanitize]
print(mask)

print( len( students[mask] ) )
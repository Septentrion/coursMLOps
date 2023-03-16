

def maxListIndice(l):
    assert type(l) == list and len(l) > 0
    
    m = l.pop(0)
    
    for e in l:
        if e > m :
            m = e
    
    return {'m' : m, 'i' : l.index(m) + 1}

try:
    print( maxListIndice([9,11,19, 6, 8, 67, 98, 15, 7000]) )
    print( maxListIndice("") )
except AssertionError:
    print("error")

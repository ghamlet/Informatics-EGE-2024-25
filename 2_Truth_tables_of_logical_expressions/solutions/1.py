#№ 18307 (Уровень: Базовый)

from itertools import product, permutations

def f(a,b,c,d):
    return ((a or b) <= ((not c) and a)) and d

for x1,x2,x3,x4,x5,x6 in product([0,1], repeat=6):

    table = [
        (1, 1, x1, 1,1),
        (1,x2,1,x3,1),
        (x4, x5, x6, 1, 1)
    ]
    
    if len(table) == len(set(table)):
        for p in permutations("abcd", r=4):
            if all(f(**dict(zip(p, row))) == row[-1] for row in table):
                print(*p)
# № 13089 (Уровень: Базовый)
from itertools import product, permutations

def f(u,w,x,y,z):
    return ((z<=w) and (y == (not x))) <= (u == (y or z))


for x1,x2,x3,x4,x5,x6,x7,x8 in product([0,1], repeat=8):
    table = [
        (0, x1, 0,0, 0,0),
        (0, x2, x3 ,0,0,0),
        (x4, 0,0,0,x5, 0),
        (0,0,x6,x7,x8,0)
    ]
    
    if len(table) == len(set(table)):
        for p in permutations("uwxyz", r=5):
            if all(f(**dict(zip(p, row))) == row[-1] for row in table):
                print(*p)
from itertools import *

def f(x,y,w,z):
    return w or (y<=z) and x


for x1,x2,x3,x4,x5,x6 in product([0,1], repeat=6):
    table = [
        (x1,x2,0,0,1),
        (1,1,x3,x4,0),
        (1,x5,x6,1,0)
    ]
    
    if len(table) ==len(set(table)):
        for p in permutations("xywz", r=4):
            if all(f(**dict(zip(p, row)) ) == row[-1] for row in table):
                print(*p)
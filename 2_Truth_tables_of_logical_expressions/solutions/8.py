from itertools import *

def f1(x,y,z,w):
    return (w<=y) == (z<=x) 

def f2(x,y,z,w):
    return (w<=y) and ((not x )==z)


for x1,x2,x3,x4,x5 in product([0,1], repeat=5):
    table = [
        (0,x1,0,0,0,1),
        (0,0,0,x2,0,x3),
        (0,1,1,x4,x5,0)
    ]
    
    if len(table) == len(set(table)):
        
        for p in permutations("xyzw", r=4):
            if all(f1(**dict(zip(p, row))) == row[-2]  and f2(**dict(zip(p, row))) == row[-1] for row in table):
                print(*p)
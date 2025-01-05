from itertools import *

def f(p1, p2, p3,p4):
    return (p3 <= p1) <= (p4 or (not p2))

print("x y z w")

for x1,x2,x3,x4 in product([0,1], repeat=4):
    table = [
        (0,0,x1,1,0),
        (0,1,x2,1,0),
        (1,1,x3,x4,0)
    ]
    
    if len(table) == len(set(table)):
        for p in permutations("p1 p2 p3 p4".split()):
            if all(f(**dict(zip(p,row))) ==row[-1] for row in table):
                print(*p)
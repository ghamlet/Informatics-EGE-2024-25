from itertools import product, permutations

def f1(x,y,z,w):
    return (w<=y) == (x and z)

def f2(x,y,z,w):
    return (not x) or (not y) or (not z) or w

def f3(x,y,z,w):
    return (z or w) and y and x


table_1 = [(1,0,1,0,1)]
table_2 = [(0,1,1,1,0)]
table_3 = [(1,1,1,0,1)]

for p in permutations("xyzw"):
    if  all(f1(**dict(zip(p, row))) == row[-1] for row in table_1) and \
        all(f2(**dict(zip(p, row))) == row[-1] for row in table_2) and \
        all(f3(**dict(zip(p, row))) == row[-1] for row in table_3):
        print(*p)
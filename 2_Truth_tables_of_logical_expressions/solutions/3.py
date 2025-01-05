from itertools import product, permutations

def f(x,y,z,w):
    return ((x<= y) or (z == x)) and (w<=z)


table= [
    (0,0,1,1,1),
    (0,0,1,0,0),
    (0,1,1,1,0)
] 

for p in permutations("xyzw"):
    if all(f(**dict(zip(p,row)))== row[-1] for row in table):
        print(*p)
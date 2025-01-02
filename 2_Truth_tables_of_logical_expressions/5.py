from itertools import *

def f(x,y,z):
    return x <= (y and z)

table = [
    (0,1,0,0),
    (1,1,0,0)
]

k =0
for p in permutations("xyz", r=3):
    if all(f(**dict(zip(p, row))) == row[-1] for row in table):
        print(*p)
        k += 1
        
print(k)
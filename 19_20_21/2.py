# Задача про фишки

from functools import  *

@lru_cache(None)
def f(x, y):
    if (x **2 + y**2) **0.5 >= 20:
        return  0

    moves = [f(x+2, y),  f(x, y+3)]
    pw = [i for i in moves if i <=0]
    if pw:
        return -max(pw)+1
    else: return -max(moves)

for i in range(1,20):
    if f(5, i) == -1:
        print(i)
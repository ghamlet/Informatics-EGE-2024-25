from functools import *

@lru_cache(None)
def f(a,b):
    if a+b >= 124: return 0

    moves = [f(a+1, b), f(a, b+1),
             f(a+3, b),  f(a, b+3),
             f(a+b, b), f(a, b+a)]

    pw = [i for i in moves if i <=0]
    if pw:
        return  -max(pw) +1
    else: return -max(moves)

# 19
for i in range(1,111):
    if f(13, i) == -1:
        print(i)

# 20
m = []
for i in range(1,111):
    if f(13, i) == 2:
        m.append(i)
print(sum(m))


# 21
for i in range(1,111):
    if f(13, i) == -2:
        print(i)
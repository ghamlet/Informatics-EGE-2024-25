from functools import lru_cache

@lru_cache(None)
def f(a,b):
    # условие завершения игры
    if a+b >= 169:
        return 0

    # возможные ходы
    moves = [f(a+4, b), f(a, b+4),
             f(a*2, b), f(a,b*2),
             f(a*3, b), f(a,b*3)]

    pw = [i for i in moves if i <=0]

    if pw:
        return  -max(pw) +1
    else:
        return -max(moves)

for i in range(1, 153):
    if f(15, i) == -1:
        print(i)
        break
from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if a + b >= 95:
        return 0

    moves = [f(a + 2, b), f(a * 3, b),
             f(a, b + 2), f(a, b * 3)]

    pw = [i for i in moves if i <= 0]
    if pw:
        return -max(pw) + 1
    else:
        return -max(moves)


# Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
for i in range(1,89):
    if f(6+2,1)==1 or f(6*3,i)==1 or f(6,i+2)==1 or f(6,i*3) ==1:
        print(i)
        break
# Обозначим через ТРЕУГ(𝑛,𝑚,𝑘)ТРЕУГ(n,m,k) утверждение «существует невырожденный треугольник с длинами сторон 𝑛n, 𝑚m и 𝑘k». Для какого наибольшего натурального числа 𝐴A формулаТРЕУГ(𝐴,7,𝑥)→((МАКС(𝑥+5,14)⩽27)≡¬ТРЕУГ(36,21,𝑥))ТРЕУГ(A,7,x)→((МАКС(x+5,14)⩽27)≡¬ТРЕУГ(36,21,x))

def triangle(n,m,k):
    # треугольник существует если выполняется условие что каждая сторона меньше суммы двух других сторон
    return (n+m > k) and (n+k > m) and (m+k >n)


def f(x):
    return triangle(A,7,x) <= ((max(x+5, 14) <= 27) == (not(triangle(36,21,x))))

for A in range(1,777):
    if all(f(x) for x in range(1,777)):
        print(A)
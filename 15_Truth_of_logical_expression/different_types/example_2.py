from math import gcd     # наибольший общий делитель

# Алгоритм Евклида
def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def f(x):
    return (gcd(A, 420) == 2) or (gcd(A, x)!=12) <= (gcd(110,x)!=11)


c = 0
for A in range(1, 1001):    # в условии Сколько существует натуральных значений A на отрезке [1; 1000]
    if all(f(x) for x in range(1,777)):
        c+=1
        
print(c)


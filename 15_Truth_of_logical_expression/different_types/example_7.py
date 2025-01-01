# Обозначим через УГОЛ(a, b, c) утверждение «значения чисел a, b, c являются углами невырожденного треугольника»

def angle(a,b,c):
    return (a + b + c == 180)

def f(x):
    return angle(37, A, x+45) == (angle(A, x, 90) and (not(A + 23 < 120)))

for A in range(1, 444):
    if all(f(x) for x in range(1, 444)):
        print(A)
# Обозначим ПЛОЩ(a, b, c) утверждение «Площадь прямоугольника со сторонами a и b больше c». Найдите наибольшее целое значение А, при котором выражение

def ploshad(a, b, c):
    return a * b > c

def f(x, y):
    return (not(ploshad(x, y, A+13))) <= ((ploshad(28, y, 520)) or (ploshad(x, 25,800)))

for A in range(-333, 333):
    if all(f(x,y) for x in range(1, 333) for y in range(1, 333)):
        print(A)
        
# Обозначим через mod(𝑚,𝑛)mod(m,n) остаток от деления m на n. Для какого наименьшего натурального числа А выражение

def mod(m,n):
    return m % n

def f(x):
    return (A +x > 700 -A) and (mod(A,100) + mod(100, x) > 50)

for A in range(1, 777):
    if all(f(x) for x in range(1, 777)):
        print(A)
        break
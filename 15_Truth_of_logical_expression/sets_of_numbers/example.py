# На один прототип есть два разных(но несильно) шаблона

# 1) Нахождение максимального количества элементов множества А (оно же и наибольшее произведение)

def f(x):
    P = {i for i in range(2, 21, 2)}    # удобно заполнить генератор если множество - арифметическая последовательность
    Q = {i for i in range(3, 31, 3)}
    
    return ((x in A) <= (x in P)) and ((not(x in Q)) <= (not(x in A)))

# так как надо найти наибольшое число элементов A то заполняем его максимальным количеством
A = set(i for i in range(1, 40))

for x in range(1, 40):
    if not(f(x)):    # проверяем каждое число из A и если при этом выражение ложно то удаляем из множества данное число
        A.remove(x)

print(len(A)) 



##----------------------------------

# 2) Нахождение минимального количества элементов множества А (оно же и наименьшее произведение)

from math import prod

def f(x):
    P = {1, 3 ,4 ,9 ,11, 13, 15, 17, 19 ,21}  
    Q = {i for i in range(3, 31, 3)}
    
    return ((x in  P) <= (x in A)) or ((not(x in A)) <= ((not(x in Q))))

# так как надо найти наименьшее число элементов A то создаем его пустым и начинаем постепенно заполнять

A = set()  # делать A = {} нельзя так как получится словарь у которого нет атрибута add

for x in range(1, 33):
    if not(f(x)):    
        A.add(x)

print(prod(A))
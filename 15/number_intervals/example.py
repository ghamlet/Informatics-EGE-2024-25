# 1) Вариант (супер быстрый)
# Наименьшая длина отрезка А

def f(x):
    P = list(range(15, 41))
    Q = list(range(21, 63))

    return ( x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))


A = []

for x in range(1, 66):
    if not(f(x)):
        A.append(x)


# внимательно !!!
print(A[-1] - A[0])  # длина отрезка
print(len(A))         # количество точек



#---------------------------------------------
# Наибольшая длина отрезка А

def f(x):
    C = list(range(48, 95))
    J = list(range(83, 101))

    return (not((x in C) or (x in J))) <= (not(x in A))


A = list(range(1, 111))

for x in range(1, 111):
    if not(f(x)):
        A.remove(x)

print(A[-1] - A[0])



#-----------------------------------------------
# 2) Вариант

def f(x):
    P = 15 <=x<= 40   
    Q = 21 <=x<= 62
    A = a1 <=x<= a2   

    return P <= ((Q and (not(A))) <= (not(P)))


min_len_otr = float("inf")     # + бесконечность для поиска минимального числа
m = []

for a1 in range(1, 66):
    for a2 in range(a1, 66):
        if all(f(x) for x in range(1, 66)):
            min_len_otr = min(min_len_otr, a2 - a1)
            
        
print(min_len_otr)

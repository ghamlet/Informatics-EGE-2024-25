
# https://www.youtube.com/watch?v=xL0DCeC7DjY

def f(x):
    P = 3 <=x<= 15
    Q = 14 <=x<= 25
    A = a1 <=x<= a2

    return (P == Q) <= (not A)


POINTS = [y for x in [3, 15, 14, 25] for y in [x-0.1, x, x+0.1]]

r = []

for a1 in POINTS:
    for a2 in POINTS:
        if a2 >= a1 and all(f(x)==1 for x in POINTS):
            r += [a2 - a1]
            
print(round(max(r)))


















# # 1) Вариант (супер быстрый)
# # Наименьшая длина отрезка А

# def f(x):
#     P = list(range(15, 41))
#     Q = list(range(21, 63))

#     return ( x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))


# A = []



# for x in range(1, 66):
#     if not(f(x)):
#         A.append(x)


# # внимательно !!!
# print(A[-1] - A[0])  # длина отрезка
# print(len(A))         # количество точек



# #---------------------------------------------
# # Наибольшая длина отрезка А

# def f(x):
#     C = list(range(48, 95))
#     J = list(range(83, 101))

#     return (not((x in C) or (x in J))) <= (not(x in A))


# A = list(range(1, 111))

# for x in range(1, 111):
#     if not(f(x)):
#         A.remove(x)

# print(A[-1] - A[0])

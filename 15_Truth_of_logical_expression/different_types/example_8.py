# Пусть P – множество всех 8-битовых цепочек, начинающихся с 11,  Q – множество всех 8-битовых цепочек, оканчивающихся на 0, а A – некоторое множество произвольных 8-битовых цепочек. Сколько элементов содержит минимальное множество A, при котором для любой 8-битовой цепочки x истинно выражение

from itertools import *


P = {"11" + "".join(bit_6) for bit_6 in product("01", repeat=6)}
Q = {"".join(bit_7) + "0" for bit_7 in product("01", repeat=7)}
X = {"".join(bit_8) for bit_8 in product("01", repeat=8)}    # для любого x

A = set()     # A минимальной длины

def f(x):
    return (not(x in A)) <= ((x in P) or (not(x in Q)))

for x in X:
    if not(f(x)):
        A.add(x)
        
print(len(A))
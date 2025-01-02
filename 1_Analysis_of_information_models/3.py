# № 17772 (Уровень: Базовый)

from itertools import *

table = "0101000 1001010 0000110 1100011 0010010 0111101 0001010".split()
graph = "AB AV BV VG VE VD DE GE GK EK".split()

print("1 2 3 4 5 6 7")

for p in permutations("ABVGDEK"):
    if all(int(table[p.index(top_1)][p.index(top_2)]) for top_1, top_2 in graph):
        print(*p)
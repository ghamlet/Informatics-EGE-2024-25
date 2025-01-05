# № 18575 (Уровень: Базовый) 

from itertools import permutations

table = "26 147 456 236 37 134 25".split()
graph = "AB AD AG DE BC GF FE DC BG".split()

print("1 2 3 4 5 6 7")

for p in permutations("ABCDEFG"):
    if all(str(p.index(top_2)+1) in table[p.index(top_1)] for top_1, top_2 in graph):
        print(*p)
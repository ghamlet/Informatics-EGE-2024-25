# № 18481 (Уровень: Базовый)

from itertools import permutations

table = "67 567 457 35 234 12 123".split()
graph = "FD FG GE DE DB BA BC EC AC".split()

print("1 2 3 4 5 6 7")

for p in permutations("ABCDEFG"):
    if all(str(p.index(top_2)+1) in table[p.index(top_1) ] for top_1, top_2 in graph):
        print(*p)
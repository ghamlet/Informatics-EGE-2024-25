# № 6254 Danov2302 (Уровень: Сложный)

from itertools import permutations

table = "0001001 0000101 0001100 1010010 0110010 0001101 1100010".split()
graph = "AG GF FB BD DE EA GC CE BC".split()

print("1 2 3 4 5 6 7")

for p in permutations("ABCDEFG"):
    if all(int(table[p.index(top_1)][p.index(top_2)]) for top_1, top_2 in graph):
        print(*p)
        
        # будет 3 варианта расположения пунктов и надо просто проверить каждый из трех
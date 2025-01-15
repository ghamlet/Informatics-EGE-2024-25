from itertools import permutations

table = "00100001 00001001 10010100 00100100 01000010 00110010 00001101 11000010".split()
graph = "DE DB BE BG EA AH GH GF HC CF".split()

print("1 2 3 4 5 6 7 8")

for p in permutations("ABCDEFGH"):
    if all(int(table[p.index(top_1)][p.index(top_2)]) for top_1, top_2 in graph):
        print(*p)
        
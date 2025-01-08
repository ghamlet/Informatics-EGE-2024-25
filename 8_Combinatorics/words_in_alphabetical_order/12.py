from itertools import product

k = 1

for p in product(sorted(set("СУБЛИМАЦИЯ")), repeat=5):
    word = "".join(p)
    
    if k %2 and word[-1] != "Я" and sum(word.count(g) for g in "УИАЯ") ==2:
        print(k)
    
    k+=1
from itertools import product

k = 0

for p in product(set("ЛЮСТРА"), repeat=5):
    word = "".join(p)
    
    if word.count("Ю") <=2 and word[-1] not in "ЛСТР":
        k+=1

print(k)


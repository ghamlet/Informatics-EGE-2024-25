from itertools import product

k = 0

for p in product(set("ВЬЮГА"), repeat=6):
    word = "".join(p)
    if "ЮГ" in word:
        k+=1
        
print(k)
    
    
from itertools import product

k = 1

for p in product(sorted(set("МАРКСЛ")),repeat=6):
    word = "".join(p)
    
    if "КС" not in word and "СК" not in word and len(set(word)) == 4:
        print(k)
    
    k+=1
    

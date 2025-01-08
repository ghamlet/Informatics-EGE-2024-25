from itertools import product

k = 0
for p in product(sorted(set("АКЛМНЯ")), repeat=5):
    word = "".join(p)
    
    if word.startswith("МН"):
        k+=1
        
print(k-2)
from itertools import product

k = 0

for p in product(set("АЛГОРИТМ"), repeat=6):
    word = "".join(p)
    
    if word.count("Л") <=1 and word[0] !="Р" and word[-1] not in "ЛГРТМ":
        k+=1
        
print(k)
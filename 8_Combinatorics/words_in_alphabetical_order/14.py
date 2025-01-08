from itertools import product

k = 1
find = True

for p in product(sorted(set("НОРМАЛЬЕ")), repeat=6):
    word = "".join(p)
    
    if word.startswith("НОРМ") and find:
        start_ind = k
        find = False
        
    if word == "НЕНОРМ":
        end_ind = k
        
    k+=1
    
print(start_ind -end_ind -1 )
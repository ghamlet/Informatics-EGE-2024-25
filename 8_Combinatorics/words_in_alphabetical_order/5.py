from itertools import product

k = 1
sogl = "МНС"
glasn = "ИУ"

for p in product(sorted(set("МИНУС")), repeat=4):
    word = "".join(p)
    if sum(word.count(ch) for ch in sogl)  >=  sum(word.count(ch) for ch in glasn):
        print(k, word)
        
    k+=1
    

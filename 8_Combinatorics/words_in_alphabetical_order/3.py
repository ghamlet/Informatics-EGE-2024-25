from itertools import product

k = 1

for p in product(sorted(set("КОДИМ")), repeat=5):
    word = "".join(p)
    
    if word.count("М")==2 and "ММ" not in word:
        print(k, word)
        
    k+=1
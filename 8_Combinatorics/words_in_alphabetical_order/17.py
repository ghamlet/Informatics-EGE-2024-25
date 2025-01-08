from itertools import product

k =1

for p in product(sorted(set("БАРАШ")), repeat=5):
    word = "".join(p)
    
    if sum(word.count(sogl) for sogl in "БРШ") <=3 and len(set(word)) ==4:
        print(k)
    k+=1
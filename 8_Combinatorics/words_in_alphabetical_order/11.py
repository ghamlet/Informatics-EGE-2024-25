from itertools import product

k = 1
print(sorted("АРГУМЕНТ"))

for p in product(sorted(set("АРГУМЕНТ")),repeat=4 ):
    word = "".join(p)
    
    if len(word) == len(set(word)) and word == "".join(sorted(word)):
        print(k, word)
        
    k+=1
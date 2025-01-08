from itertools import product

k = 1

for p in product(sorted(set("павсикакий".upper())), repeat=6):
    word = "".join(p)
    
    if word == "КАКААА":
        print(k)
      
    if any(True for comb in product("АИ", repeat=2) if  "".join(comb) in word):
        k+=1      
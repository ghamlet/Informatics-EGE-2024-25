from itertools import product

k = 1

for p in product("ГЕКЭ023", repeat=4):
    word = "".join(p)
    
    if word[0] in "023" and all(word[i] != word[i+1] for i in range(len(word)-1)):
        print(k)
        break
        
    k+=1
    

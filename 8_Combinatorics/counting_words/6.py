from itertools import product

k = 0
c =set()

for p in product(set("ВОРОБЕЙ"), repeat=5):
    word = ''.join(p)
    
    if word[0] != "Й" and word[-1] !="Й" and word.count("Й") <=1 and (not "ЕЙ"  in  word) and (not "ЙЕ"  in  word):
        k+=1
        c.add(word)
        
        
print(k)
print(c)
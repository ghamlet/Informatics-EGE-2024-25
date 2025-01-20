from itertools import product

k = 1

for p in product(sorted("АКРУ"), repeat=5):
    word = "".join(p)
    
    if word in ["РУКАА", "УКАРА"]:
        print(k)
        
    k+=1

        
print(841 - 721 +1)
    

from itertools import product

k = 0

for p in product("0123456789AB", repeat=5):
    number = "".join(p)
    
    if number[0] != "0" and number.count("7") ==1 and sum([number.count(d) for d in "9AB"]) <=3:
        k+=1
        
print(k)
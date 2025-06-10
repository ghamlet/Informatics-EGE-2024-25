from itertools import product

k = 0

for number in product("012345678", repeat=7):
    number = "".join(number)
    
    if number[0] not in "0246" and len(set(number[-3:])) != 1:
        k+=1
        
print(k)
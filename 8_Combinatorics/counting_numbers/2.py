from itertools import product

k = 0

# 1 способ
for number in product(range(12), repeat=6):
    
    if number[0] != 0 and number.count(11) == 1 and  len([d for d in number if d %2 ==0]) ==3:
        k+=1
        
        
print(k)


# 2 сопособ
k = 0

for p in product("0123456789AB", repeat=6):
    number = "".join(p)
    
    if number[0] != "0" and number.count("B") ==1 and len([d for d in number if d in "02468A"]) == 3:
        k+=1
        
print(k)

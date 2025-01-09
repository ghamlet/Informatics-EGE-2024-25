from itertools import product

k = 0
bad_list = "07 27 47 67 87 A7 70 72 74 76 78 7A".split()

for p in product("0123456789AB", repeat=5):
    number = "".join(p)
    
    if number[0] != "0" and number.count("A") == 2 and all(bad not in number for bad in bad_list):
        k+=1
        
print(k)
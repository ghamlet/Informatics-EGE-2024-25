from itertools import product

k = 0

for number in product(range(15), repeat=5):
    if number[0] != 0 and number.count(8) == 1 and len([d for d in number if d > 9]) >=2:
        k+=1
        
print(k)
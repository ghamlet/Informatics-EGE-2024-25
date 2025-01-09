from itertools import product

k = 0

for number in product(range(7), repeat=7):
    if number[0] !=0 and len([d for d in number if d%2==0]) ==2:
        k+=1
        
print(k)
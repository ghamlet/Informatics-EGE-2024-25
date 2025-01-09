from itertools import product

k =0

for number in product(range(14), repeat=5):
    if number[0]!=0 and len(set(number)) ==2 and (number[-1] == 0 or number[-1] == 3):
        k+=1
        
print(k)
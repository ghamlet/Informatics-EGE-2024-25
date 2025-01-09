from itertools import product

k=0

for number in product(range(20), repeat=5):
    
    if number[0] !=0 and (number[0] + number[-1] ==26) and all(number[i]%2!=number[i+1]%2 for i in range(4)):
        k+=1
print(k)    
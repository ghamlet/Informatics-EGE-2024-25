from itertools import product

k = 0

for number in product(range(9), repeat=7):    
    if number[0] and number.count(6)==1 and all(number[i] %2 != number[i+1] %2  for i in range(len(number)-1)):
        k+=1
        
print(k)
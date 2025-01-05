min_ = 99999

for n in range(1,666):
    n2 = bin(n)[2:]
    
    if len(n2) % 2 ==0:
        n2 += "1"
    else:
        n2 = "1" + n2 + "0"
        
    R = int(n2, 2)
    if R > 666:
        min_ = min(R, min_)
        
print(min_)
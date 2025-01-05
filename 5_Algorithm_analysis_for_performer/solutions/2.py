m = []

for n in range(1,26):
    n2 = bin(n)[2:]
    
    if n%2:
        n2 = "10" + n2 +"1"
        
    else:
        n2 = "10" + n2 +"0111"
        
    R = int(n2, 2)
    m.append(R)
    
print(max(m))
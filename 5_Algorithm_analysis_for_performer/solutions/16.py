for n in range(1, 11111):
    nb = bin(n)[2:]
    
    if n%2==0:
        nb+="10"
    else:
        nb = "1" + nb+"01"
        
    r = int(nb, 2)
    
    if r > 516:
        print(n)
        break

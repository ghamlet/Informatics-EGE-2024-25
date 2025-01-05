for n in range(1, 1111):
    n2 = bin(n)[2:]
    
    if sum(map(int, n2)) % 2==0:   # если сумма цифр в двоичной записи числа чётная
        n2 +="0"
        n2 = "10" + n2[2:]
    else:
        n2 +="1"
        n2 = "11" + n2[2:]
        
    R = int(n2,2)
    if R > 171:
        print(n)
        break
        
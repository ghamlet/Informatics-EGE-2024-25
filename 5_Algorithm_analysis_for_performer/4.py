def chetvert(x):
    s = ""
    
    while x>0:
        s += str(x % 4)
        x= x // 4
        
    return s[::-1]

for n in range(1, 1111):
    n4 = chetvert(n)
    
    if n%4 ==0:
        n4 = "2"+ n4 +"03"
    else:
       n4 += chetvert(( n % 4) * 5)
       
       
    R = int(n4, 4)
    if R < 568:
        print(n)
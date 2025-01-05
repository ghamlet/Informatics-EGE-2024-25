def tri(x):
    s =""
    while x >0:
        s += str(x % 3)
        x = x // 3
        
    return s[::-1]


for n in range(1, 1111):
    n3 = tri(n)
    
    if n % 3 ==0:
        n3 += n3[-2:]
    else:
       n3 += tri(sum(map(int, n3)))
       
    R = int(n3, 3)
    
    if R > 220 and R % 2 ==0:
        print(R)
        break
    
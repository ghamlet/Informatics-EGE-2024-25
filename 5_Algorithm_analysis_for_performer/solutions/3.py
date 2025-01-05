def tri(x):
    s = ""
    
    while x >0:
        s += str(x%3)
        x = x//3
        
    return s[::-1]

for n in range(4,1111):
    n3 = tri(n)
    
    if n3[-2:] == "10":
        n3 = "2" + n3
    else:
        n3 = "1" +n3
        
    R = int(n3,3)
    if R > 130:
        print(n)
        break
for n in range(1,111111111):
    
    s1 = sum(int(d) for d in str(n) if int(d)%2!=0)
    s2 = sum(int(d) for i, d in enumerate(str(n)) if (len(str(n)) -i-1) %2==0)
    
    r = abs(s1-s2)
    if r ==29:
        print(n)
        break
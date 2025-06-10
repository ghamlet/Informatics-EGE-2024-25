def dev(x):
    c= set()
    for i in range(1, int(x**0.5)+1):
        if x % i ==0:
            c.add(i)
            c.add(x//i)

    return c

k=0
for x in range(1_125_000, 11_111_111):
    devs = dev(x)
    
    ok_7 = [d for d in devs  if d % 10 ==7 and d != x and d !=7]
    if ok_7:
        k+=1
        minn = min(ok_7)
        print(x, minn)


    if k==5:
        break

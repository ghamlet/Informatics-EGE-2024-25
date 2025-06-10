
for x in range(77777777):
    n = 3**200 + 3**10 - x

    c= 0
    while n:
        if n%3==2:
            c+=1
        n//=3

    if c==200:
        print(x)


f = open("17_21712.txt")
a = [int(x) for x in f]

ans = []
min6 = min(x for x in a if  (1000<= abs(x) < 10_000) and abs(x) %10 ==6 and x >0)
k=0
for a,b,c in zip(a, a[1:], a[2:]):
    t = [x for x in [a,b,c] if  (1000<= abs(x) < 10_000) and abs(x) %10 ==6]
    summa= a+b+c
    if len(t) ==1 and summa <=min6:
        k+=1
        ans.append(summa)

print(k, max(ans))

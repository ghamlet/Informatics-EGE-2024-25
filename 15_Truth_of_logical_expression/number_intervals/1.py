def f(x):
    B = 36<=x<=75
    C = 60<=x<=110
    A = a1<=x<=a2

    return  (not(A) )<= (B==C)

ans = []
p = [y for x in [36,75,60,110] for y in[x, x-0.1, x+0.1] ]

for a1 in p:
    for a2 in p:
        if a2>a1 and all(f(x) for x in p):
            ans.append(a2-a1)

print(min(ans))


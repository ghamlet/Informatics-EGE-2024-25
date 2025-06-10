f = open("9_21895.csv")
c=0
for i in f:
    a = sorted(list(map(int, i.split(";"))))
    print(a)

    if len(set(a)) ==5:
        if a[-1] + a[-2] <= a[0] + a[1]+a[2]:
            c+=1

print(c)
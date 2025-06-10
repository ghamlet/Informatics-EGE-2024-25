f = open("9_21704.csv")
c=0
for i in f:
    a = list(map(int, i.split(";")))
    print(a)

    if a == sorted(a, reverse=True):
        print(a)
        s = sum(a)
        ma =max(a)
        mi = min(a)
        ost = s -ma - mi

        if ((ma+mi)/2 ) > ( ost /5):
            summ = sum(a)
            break
print(summ  )
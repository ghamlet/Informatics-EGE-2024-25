f = open("9_21408.csv")
c=0
for i in f:
    a= list(map(int, i.split(";")))
    a3 = [i for i in a if a.count(i)==3]
    nepov = [i for i in a if a.count(i)==1]

    if len(a3)==6:
        if max(a3) > nepov[0]:
            c+=1

print(c)
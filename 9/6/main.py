f = open("9_20955.csv")
k=0
for i  in f:
    a= list(map(int, i.split(";")))
    a2 = [i for i in a if a.count(i) ==2]
    a1 =  [i for i in a if a.count(i) ==1]



    if len(a2) ==4 and len(a1)==4:
        if sum(a2) /sum(a1) >=2:
            k+=1

print(k)
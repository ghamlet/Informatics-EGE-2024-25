f = open("9.csv")
c =0

for line in f:
    a = list(map(int, line.split(",")))
    nepov = [i for i in a if a.count(i)==1]
    pov = [i for i in a if a.count(i)==3]
    if len(nepov)==3 and len(pov) ==3:
        sr = sum(nepov) / len(nepov)
        su = sum(pov)

        if sr < su:
            c+=1

print(c)

# 125
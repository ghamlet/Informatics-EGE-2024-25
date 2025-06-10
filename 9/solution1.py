f = open("9/exel.txt")
c = 0

for line in f:
    line = list(map(int, line.split()))

    if sum(line) > 475 and sum(x for x in line if x %2==0) <50:
        c+=1

print(c)
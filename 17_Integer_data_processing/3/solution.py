f = open("17_Integer_data_processing/3/Задание_17__gmt2__gt88__sqyl.txt")

m = [int(i) for i in f]
k = 0
maxx = -float("inf")

for i in range(len(m)-1):
    if bin(m[i])[2:].count("1") >=5 or bin(m[i+1])[2:].count("1") >=5:
        k+=1
        maxx = max(maxx, m[i]+m[i+1])
        
print(k, maxx)
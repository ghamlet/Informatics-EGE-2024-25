f = open("17_Integer_data_processing/2/4__shvg.txt")

m = [int(i) for i in f]
k = 0
maxx = -float("inf")

for i in range(len(m)-1):
    if abs(m[i] - m[i+1]) % 42==0:
        k+=1
        maxx = max(maxx, m[i] +m[i+1])
        
print(k, maxx)
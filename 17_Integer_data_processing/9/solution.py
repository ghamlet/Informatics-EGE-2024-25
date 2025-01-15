f = open("17_Integer_data_processing/9/17__1ssk3.txt")
m = [int(i) for i in f]
k = 0
maxx = -100000000500000000

k24 = min(i for i in m if i % 24==0)


for i in range(len(m)):
    for j in range(i+1, len(m)):
        if m[i] % k24 ==0 or m[j] % k24 ==0:
            k+=1
            maxx = max(maxx, m[i]+m[j])
            
print(k, maxx)

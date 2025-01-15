f = open("17_Integer_data_processing/5/17_4__1kacf.txt")

m = [int(i) for i in f]
k = 0
minn = 10000000005000000000

for i in range(len(m)-1):
    if  all(int(d) %2==0  for d in str(m[i])) and all(int(d) %2==0  for d in str(m[i+1])):
        k+=1
        minn = min(minn, m[i] + m[i+1])
        
print(k, minn)
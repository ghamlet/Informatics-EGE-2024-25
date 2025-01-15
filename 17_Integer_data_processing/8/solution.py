f = open("17_Integer_data_processing/8/17__1nxre.txt")
m = [int(i) for i in f]
k = 0
minn = 10000005000000

for i in range(len(m)-1):
    if  (all(int(d) %2==0 for d in str(m[i])) and all(int(d) %2==0 for d in str(m[i+1]))) or \
        (all(int(d) %2!=0 for d in str(m[i])) and all(int(d) %2!=0 for d in str(m[i+1]))):
            k+=1
            minn = min(minn, m[i]+m[i+1])
            
print(k, minn)
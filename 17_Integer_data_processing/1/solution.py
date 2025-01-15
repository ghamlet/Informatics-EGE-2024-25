f = open("17_Integer_data_processing/1/Задание_17__f6wj__rnth.txt")

m = [int(num) for num in f]
ost = sum(m) % 100000
k = 0

minn = 1000005000000000

for i in range(len(m)-1):
    if ( m[i] > ost and m[i+1] < ost and m[i+1]%100 ==99 ) or ( m[i] < ost and m[i+1] > ost and m[i]%100 ==99):
        k+=1
        minn = min(minn, m[i]+m[i+1])
        
        
print(k, minn)
        
        
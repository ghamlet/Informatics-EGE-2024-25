f = open("/home/arrma/programms/Informatics-EGE-2024-25/17_Integer_data_processing/4/Задание_17__t43z.txt")

m = [int(i) for i in f]
k = 0
maxx = -float("inf")


def convert(x):
    a = "0123456789ABCDEF"
    s = ""
    while x > 0:
        s = a[x%16] + s 
        x = x//16
        
    return s

for i in range(len(m)-1):
    if (convert(abs(m[i] * m[i+1])))[-1] == "E" and len([j for j in [ m[i] , m[i+1]] if abs(j) %10 ==6]) ==1:
        k+=1
        maxx = max(maxx, m[i]+m[i+1])
        
print(k, maxx)
print(-11%5)
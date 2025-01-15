f = open("17_Integer_data_processing/7/4__1n2ut.txt")
m = [int(i) for i in f]
k = 0
sum_gip = 0

for i in range(len(m)-2):
    a,b,c = m[i:i+3]
    
    if (a+b>c ) and (a+c>b) and (b+c>a) \
    and ((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)):
        k+=1
        sum_gip+=max(m[i], m[i+1] , m[i+2])
        
print(k, sum_gip)
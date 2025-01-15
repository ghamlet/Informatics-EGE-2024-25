f = open('22/1.txt')

times =[]
a =[]
res = [0] * 40

for s in f:
    s = s.split()
    times.append(int(s[0]))
    s=s[1:][0]
    s = list(map(int, s.split(';')))
    a.append(s)

for i in range(len(times)):
    if len(a[i]) == 1 and a[i][0] ==0 :
        res[i] = times[i]

    else:
        m = 0
        for elem in a[i]:
            m= max(m, res[elem-1])
        res[i] = m + times[i]
        
print(times)
print(a)
print(res)
print(max(res))




# arr =[0] *44

# for s in f.readlines():
#     number, time, need = s.rstrip().split("\t")
#     # arr.append(0)
    
#     print(need.split(";"))
    
#     for j in need.split(";"):
#         arr[int(number)] = max(arr[int(number)], arr[int(j)])
        
#     arr[int(number)]+=int(time)
    
# print(arr)
# print(max(arr))
# В текстовом файле 8.txt. находится цепочка из символов латинского алфавита A, B, C, D, E.
# Найдите длину самой длинной подцепочки, не содержащей сочетания DA.

f = open("24/6/24-2__33ojc.txt").readline()

k = 0
mmax= 0

for i in range(len(f)-1):
    if f[i] =="D" and f[i+1] == "A":
        k=1
        
    else:
        k+=1
        mmax= max(mmax,k)
        
print(mmax)




s = f.replace("DA", "D A").split()
mx = 0

for i in range(len(s)):
    mx = max(mx, len(s[i]))

print(mx)

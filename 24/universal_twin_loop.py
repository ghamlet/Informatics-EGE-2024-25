# s = open('24.txt').readline()
s = "AAAAAAD12345ADDAAAA123AAAA"   # 8
m = 0

for l in range(len(s)):   # левый указатель
    for r in range(l + m, len(s)):  # m позволяет скипать короткие последовательности
        c = s[l:r+1]
        kolvo_zifr  = len([d for d in c if d in "0123456789"])

        # противное условие
        if c[0]!="D" or kolvo_zifr > 5 or c.count("D") >1:
            break

        if kolvo_zifr ==5:
            m = max(m, len(c))
            print(m, c)

print(m)


from re import  *

reg = 'D([A-CE-Z]*[0-9]){5}[A-CE-Z]*'

f = finditer(reg, s)
for i in f:
    print(i.group())


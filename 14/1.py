from string import printable

x = 17**5 + 85**8 -10

d = printable
s=''
while x:
    s = d[x%17]+s
    x//=17

print(s.count("g"))
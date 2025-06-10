from string import printable

# цифры 18 -ричной системы
alp = printable[:18]

for x in alp:
    a = int(f"9009{x}", 18) + int(f"2257{x}",18)
    if  a % 15==0:
       print(x, a//15)


for x in range(18):
    a = 9*18**4 +  9*18**1 + x
    b = 2*18**4 + 2 *18**3+5*18**2 + 7 * 18 ** 1 + x
    if (a+b) %15==0:
        print(x, (a+b) // 15)

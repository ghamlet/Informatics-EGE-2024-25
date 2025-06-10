from math import  *

alp = 10+52+458
i = ceil(log2(alp))

for l in range(1, 9999999):
    numbers = ceil(i*l/8) * 862 /1024
    if numbers <=276:
        print(l)

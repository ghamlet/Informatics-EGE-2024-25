# 4*4736*1   7993
from fnmatch import  *

for x in range(0, 10**10, 7993):
    s = str(x)
    if fnmatch(s, "4*4736*1"):

        print(x, x//7993)
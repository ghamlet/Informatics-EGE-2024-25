# from itertools import *
#
# chtn = ["".join(p) for i in range(8) for p in product("02468", repeat=i)]
# ans = []
#
# for a in "13579":
#     for b in "13579":
#         for ch in chtn:
#             if ch:
#                 if ch[0] !="0":
#                     n = int(ch + "12" + a+ "4"+b)
#
#
#                     if n <= 10**10 and n % 9231 ==0:
#                         ans.append([n, n//9231])
#
# ans = sorted(ans)
# for i in ans:
#     print(*i)


from re import *

for x in range(9231, 10**10, 9231):
    if fullmatch("[02468]*12[13579]4[13579]", str(x)):
        print(x)
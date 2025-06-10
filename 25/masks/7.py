from itertools import  product

chtn = []

for i in range(5):
    for p in product("02468", repeat=i):
        n = ''.join(p)
        chtn.append(n)

print(chtn)
ans = []
for ch in chtn:
    for a in "13579":
        for b in "13579":
            pattern = int("20" + a + b +"22" + ch)

            if pattern % 10980 ==0:
                ans.append([pattern, pattern // 10980])


ans = sorted(ans)
for i in range(5):
    print(*ans[i])
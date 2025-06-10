dv = [2 **i for i in range(20)]

ans = []
for a in range(10):
    for b in range(10):
        for d in dv:
            num = int("8902" + str(a) + str(b) + str(d))

            if num % 1432 ==0 and num <= 10**10:
                ans.append([num, num // 1432])

ans = sorted(ans)
for i in range(5):
    print(*ans[i])




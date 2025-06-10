def f(a,b,m):
    if 107 <= a+b <= 170: return m%2 ==0
    if a+b > 170: return  m%2 !=0
    if m ==0: return 0

    h = [f(a+10, b, m-1), f(a, b+10, m-1),
         f(a*2, b, m-1), f(a, b*2, m-1)]

    return any(h) if m%2 !=0 else all(h)

print(19, [s for s in range(1, 101) if f(5, s,2 )])

# 1. при котором Петя имеет выигрышную стратегию своим первым или вторым ходом, при этом Ваня должен совершить свой первый ход.
print(20, [s for s in range(1, 101) if not f(5, s,1 ) and f(5, s, 3)])
print(21, [s for s in range(1, 101) if not f(5, s,2 ) and f(5, s, 4)])


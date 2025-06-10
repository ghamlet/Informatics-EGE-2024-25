from functools import lru_cache

@lru_cache(None)
def f(n):
    if n<5: return n
    if n>=5 : return 2*n * f(n-4)

for n in range(1,13766):
    f(n)

print((f(13766) - 9 * f(13762))//f(13758))



f = {}
for n in range(14000):
    if n<5: f[n] = n
    if n>=5: f[n] = 2*n * f[n-4]

print((f[13766] - 9* f[13762]) // f[13758])

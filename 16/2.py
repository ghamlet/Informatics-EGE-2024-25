from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 2025: return n 
    if n < 2025: return f(n+1) - f(n+2) +7
    
    
    
for i in range(3333, 1,-1):
    f(i)
    
print(f(15)- f(24))
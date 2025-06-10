def f(x,y):
    return  (x+3*y> A) or (x<18) or (y<33)

for A in range(888):
    if all(f(x,y) for x in range(444) for y in range(444)):
        print(A)
def f(x,y,z):
    return (2*x +y !=136) or (z*y <100 ) or (A*A >= x+y)


for A in range(1,333):
    if all(f(x,y,z) for x in range(1, 222) for y in range(1, 222) for z in range(1, 222)):
        print(A)
        break
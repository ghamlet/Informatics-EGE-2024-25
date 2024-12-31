def f(x,y):
    return (x -3*y < A) or (y > 400) or (x >56)

for A in range(777):
    if all(f(x,y) for x in range(1, 555) for y in range(1, 555)):
        print(A)
        break

# https://www.youtube.com/watch?v=xL0DCeC7DjY

def f(x):
    B = 23 <=x<= 37
    C = 41 <=x<= 73
    A = a1 <=x<= a2

    return not(((not B) <= C ) <=A)


POINTS = [y for x in [23,37,41,73] for y in [x-0.1, x, x+0.1]]

r = []

for a1 in POINTS:
    for a2 in POINTS:
        if a2 >= a1 and all(f(x)== 0 for x in POINTS):
            r += [a2 - a1]
            
print(round(min(r)))

def f(x):
    M = list(range(32, 69))
    N = list(range(54, 77))

    return (not((x in M )or (x in N))) == (not(x in A))


A = []

for x in range(1, 88):
    if not(f(x)):
        A.append(x)


# внимательно !!!
print(A[-1] - A[0])
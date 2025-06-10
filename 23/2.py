def f(a,b,flag1, flag2):
    if a>b or a ==56: return  0
    if a == 40: flag1 =1
    if a ==72: flag2 = 1

    if a==b:
        if flag1 and flag2:
            return  1
        else: return  0

    return  f(a+3, b, flag1, flag2) + f(a+7, b, flag1, flag2) + f(a*3, b, flag1, flag2)


print(f(12, 89,0,0))


# II способ
def g(a,b):
    if a > b or a ==56: return  0
    if a == b:
        return  1

    return  g(a+3, b) + g(a+7, b) + g(a*3, b)

print(g(12, 40) * g(40, 72) * g(72, 89) )
def f(a,b,flag):
    if a>b or a==8: return  0   # условие выхода
    if a==14: flag =1 # траектория вычислений должна содержать
    if a==b:  # проверка конечного результата
        if flag: # если траектория вычислений содержала нужное число, то такая ветка нам подходит
            return 1
        else: return 0

    return  f(a+1, b, flag) + f(a+2, b, flag) + f(a*2, b, flag)

print(f(3,18,0))

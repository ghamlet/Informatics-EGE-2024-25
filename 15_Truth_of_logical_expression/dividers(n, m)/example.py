# A можно не передавать в функцию, т.к. она будет глобальной
def f(x):  
    return ((x % 7 !=7) and (x % 13 == 0)) <= (x > A -40)


for A in range(1, 555):
    if all(f(x) for x in range(1,333)):    #! важный момент: если в условии говорится что при любом натуральном значении переменной х, то перебор надо начинать с 1
        print(A)
        
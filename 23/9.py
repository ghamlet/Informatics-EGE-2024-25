def f(start, end, s):
    if start < end: return  0

    # никакая команда не повторяется более двух раз
    if start ==end and "AAA" not in s and "BBB" not in s:
        return  1

    # В. Если число четное, Разделить на 2, Иначе Вычесть 7
    return  f(start-2, end, s+"A") + f(start //2 if start %2==0 else start -7, end, s +"B")

print(f(40,1, ''))
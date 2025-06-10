
for x in range(555):
    summa = 0

    n = 81 ** 20 - 9 ** x + 50

    while n:
        summa += n % 9
        n//=9

    if summa== 138:
        print(x)
        break
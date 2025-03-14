"""№ 2514 Новогодний вариант 2021/2022 (Уровень: Сложный)
(А. Калинин) Написав секретное письмо Снегурочке, Дед Мороз уложил его конверт и принялся писать адрес, но никак не может вспомнить свой почтовый индекс.
Он помнит, что предпоследняя цифра индекса – «9», а также, что в нём содержится цифра 2. Выясните, что это за индекс,
если известно, что это наименьшее подходящее шестизначное число, поступающее в описанный ниже алгоритм, результатом которого является число «1519»

1. Попарно складываются первая и вторая цифры, третья и четвёртая, пятая и шестая, и результаты последовательно записываются друг за другом.
2. Строится двоичная запись полученного числа.
3. К полученной двоичной записи приписывается ещё один разряд по правилу:

а) Если число чётное, то приписывается 0

б) Если число нечётное, то приписывается 1

4. Полученное число переводится в десятичную систему счисления.

Показать ответ"""

for n in range(100_000, 1_000_000):
    n = str(n)
    
    summa_1 = str(int(n[0]) + int(n[1]))
    summa_2 = str(int(n[2]) + int(n[3]))
    summa_3 = str(int(n[4]) + int(n[5]))
    
    res = int(summa_1 + summa_2 + summa_3)
    bin_ = bin(res)[2:]
    
    if bin_.endswith("0"):
        bin_ += "0"
    else:
        bin_ += "1"
        
    R = int(bin_, 2)
    if R == 1519 and n[-2] == "9" and "2" in n:
        print(n)
        break
    

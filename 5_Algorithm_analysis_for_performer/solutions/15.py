"""№ 3176 Вариант от учеников (Уровень: Сложный)
На вход алгоритму Галиб-001 подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом:

1) Строится девятиричная запись числа N.
2) Подсчитывается количество пятёрок и семёрок в полученной записи. Если их количество одинаково, в конец записи добавляется её последняя цифра. В противном случае в конец записи добавляется цифра, которая встречается чаще. Если таких цифр несколько, выбирается наибольшая по значению.
3) Шаг 2 повторяется ещё четыре раза.
4) Результат переводится в шестнадцатиричную систему счисления.
При каком наибольшем исходном числе N < 10000 в результате работы алгоритма получится число, которое содержит в себе сочетание BAC?  
"""

def devyat(x):
    s = ""
    
    while x > 0:
        s += str(x % 9)
        x //=9
        
    return s[::-1]


def find_max_most_common_digit(number: str):
    m = []
    max_common_digit = 0

    for digit in range(9):
        m.append([digit, number.count(str(digit))])
        
    most_freq = max(m, key= lambda x: x[1])[1]


    for item in m:
        if item[1] == most_freq:
            max_common_digit = max(max_common_digit, item[0])
            
    return str(max_common_digit)


for n in range(10000, 1, -1):
    n9 = devyat(n)
    
    for i in range(5):
        k_5 = n9.count("5")
        k_7 = n9.count("7")
        
        if k_5 == k_7:
            n9 += n9[-1]
        else:
            d = find_max_most_common_digit(n9)
            n9 +=d
            
        
    R = int(n9, 9)
    R = hex(R)[2:]
    
    if "bac" in R:
        print(n)
        break




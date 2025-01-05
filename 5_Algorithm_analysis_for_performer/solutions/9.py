"""№ 488 Джобс 19.10.2020 (Уровень: Сложный)
Автомат обрабатывает четырехзначное десятичное число N.

Из цифр числа строятся все возможные двузначные числа путем перестановки цифр числа.
Пример.
Дано число 1223.
Из него можно построить следующие числа: 12, 13, 21, 22, 23, 31, 32.
Найдите разницу между минимальным и максимальным числами N, из цифр которых можно составить максимально возможное количество двузначных чисел.

Показать ответ"""
from itertools import *

max_len = 0
max_N = 0
min_N = 9999999

for n in range(1000, 10000):
    p = set([int(''.join(i)) for i in permutations(str(n), r=2) if i[0] != "0"] )    
    len_ = len(p)
    max_len = max(max_len, len_)
    
    
for n in range(1000, 10000):
    p = set([int(''.join(i)) for i in permutations(str(n), r=2) if i[0] != "0"] )
    len_ = len(p)

    if len_ == max_len:
        max_N = max(max_N, n)
        min_N = min(min_N, n)
     
diff = max_N - min_N
print(diff)  

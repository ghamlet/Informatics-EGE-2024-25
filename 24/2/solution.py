# В текстовом файле 9.txt находится цепочка из цифр. 
# Преобразуйте строку, так чтобы подцепочки из одинаковых элементов были заменены на 
# подцепочку из одного символа. Например, если часть строки выглядит так “111322114444”, то она заменится на “13214”.
# В ответе запишите сумму всех элементов преобразованной цепочки.


# I СПОСОБ
f = open("24/2/9__19jzs.txt").readline()

m = [f[0]]   # кладем в массив первую цифру последовательности

for digit in f:   # проходимся по каждой цифре строчки и если текущая цифра отличается от последней добавленной , то добавляем ее
    if digit != m[-1]:
        m.append(digit)
        
summ = sum(map(int, m))
print(summ)


# II СПОСОБ
prev_digit = None
uniq_elements = []

for cur_digit in f:
    if cur_digit != prev_digit:
        prev_digit = cur_digit
        uniq_elements.append(cur_digit)
        
summ = sum(map(int, uniq_elements))
print(summ)
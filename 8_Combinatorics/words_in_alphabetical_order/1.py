# № 19240 ЕГКР 21.12.24 (Уровень: Базовый)

from itertools import product

k = 1   # как в таблице
m = []

for p in product(sorted("ЯНВАРЬ"),repeat=5):
    word = "".join(p)
    
    if word[0] != "Я" and word.count("Ь") <=1 and "ЯЯ" not in word:
        m.append([k, word])
        
    k += 1

print(max(m))
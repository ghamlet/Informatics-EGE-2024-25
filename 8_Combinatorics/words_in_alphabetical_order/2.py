from itertools import product

k = 0

for p in product(sorted(set("КАЛЕЙДОСКОП"), reverse=True), repeat=6):
    word = "".join(p)
    
    if k % 2== 0 and word[0] == "К" and word.count("Й") >= 2 and "С" not in word and "Е" not in word:
        print(k, word)
        break
    
    k += 1
from itertools import product

k = 1

for p in product(sorted(set("СЕНТЯБРЬ")), repeat=5):
    word = "".join(p)
    if word[0] == "Р" and "Ь" not in word:
        print(k)
    k+=1
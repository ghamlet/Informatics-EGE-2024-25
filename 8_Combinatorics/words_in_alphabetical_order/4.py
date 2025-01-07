from itertools import product

k = 1
good_words = 0

for p in product(sorted(set("ПРЕСТОЛ")), repeat=5):
    word = "".join(p)
    
    if k % 2 !=0 and word[-1] in "ЕО" and sum(word.count(symbol) for symbol in "ПРСТЛ") <= 3:
        good_words +=1
        
    k+=1
    
print(good_words)
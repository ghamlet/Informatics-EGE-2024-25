from itertools import product

pos = 1
palindroms = {}
dif = 26655


def check_palindrom(current_word):
    
    for palindrom in palindroms.keys():
        if palindrom == current_word and pos - palindroms[palindrom] == dif:
            print(sum(map(int, str(palindroms[palindrom]))))
            exit()
    

for p in product(sorted(set("АИКЛМЬ")), repeat=6):
    current_word = "".join(p)
    
    check_palindrom(current_word)
    
    if current_word[0] == "К" and current_word[-1] == "Ь" and len(current_word) == len(set(current_word)):
        print(pos, current_word)
        
        palindroms[current_word[::-1]] = pos
        
    pos +=1
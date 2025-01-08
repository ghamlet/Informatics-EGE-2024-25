from itertools import permutations

k = 0
glasnye = "АИ"
                                                                                                                                       # 1 2      2 1
for p in set(permutations("ДЖАВАСКРИПТ", r=11)):  # одинаковые буквы в слове воспринимаются как разные и поэтому в permutations слова СОБАКА и СОБАКА будут двумя разными словами а set() оставит только СОБАКА 
    word = "".join(p)
    
    
    if sum(index +1 for glasn in glasnye  for index, char in enumerate(word) if char == glasn) == 11:
        k+=1
        
print(k)

from itertools import permutations

k = 0
sogl = ["".join(p) for p in permutations("СРТРВК", r=3)]
glasn = ["".join(p) for p in permutations("ОИАО", r=3)]
bad_list = sogl + glasn

for p in set(permutations("СОРТИРОВКА")):
    word = "".join(p)
    # word = word.replace("С", "К").replace("Р", "К").replace("Т", "К").replace("В", "К")
    # word= word.replace("И", "О").replace("А", "О")
    # if "ККК" not in word and "ООО" not in word:
    if all(word[i:i+3] not in bad_list  for i in range(len(word)-2)):
        k+=1
print(k)
    
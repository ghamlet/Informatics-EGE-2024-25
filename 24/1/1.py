#Текстовый файл 11.txt состоит не более чем из 106   заглавных латинских букв (A..Z). 
# Текст разбит на строки различной длины. Определите количество строк, 
# в которых встречается комбинация K*N, где звёздочка обозначает любой символ.


# I СПОСОБ

f = open("24/1/11__1tiye.txt")

alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
k = 0

for line in f:
    was_need_posled = False
    
    for char in alphabet:
        if "K" + char + "N" in line:
            was_need_posled = True
            
    if was_need_posled:
        k+=1
  
print(k)


# II СПОСОБ

k = 0
count_lines = 0

for line in f:
    for i in range(len(line) -2):
        if line[i]== "K" and line[i+2] == "N":
            k+=1
            
    if k > 0:
        count_lines+=1
        k = 0
        
print(count_lines)
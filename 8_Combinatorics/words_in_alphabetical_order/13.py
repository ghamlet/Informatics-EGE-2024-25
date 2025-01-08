from itertools import product

m = []
for i, p in enumerate(product(sorted('ПРИВЫЧКА'), repeat = 5)):
    if (i+1) % 5!=0:
        word = "".join(p)
        m.append(word)


for id, word in enumerate(m):
    k = id+1
    
    if len(set(word)) == len(word) and all(x in word for x in 'ПРВЧК'):
        print(k)
        break
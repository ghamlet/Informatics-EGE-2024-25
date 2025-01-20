s = "QWQWWQQW"

l =1
for i in range(len(s)-1):
    if s[i:i+2] == "QW":
        print(l)
        l=1
    else:
        l+=1
        
print(l)   
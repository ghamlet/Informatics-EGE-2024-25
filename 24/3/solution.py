# В текстовом файле 2.txt находится цепочка из символов, 
# в которую могут входить строчные буквы латинского алфавита a…z и 
# десятичные цифры. Найдите длину самой длинной подцепочки, состоящей из 
# символов одной группы (буквы или цифры).


# 123a45abcd12345

f = open("24/3/2__1vf5w.txt").readline()

len_podposled = 1
mmax_len = 1

digits = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, len(f)):
    if (f[i] in digits and f[i-1] in digits) or (f[i] in letters and f[i-1] in letters):
        len_podposled +=1
        mmax_len = max(mmax_len, len_podposled)

    else:
        len_podposled = 1
        
print(mmax_len)



was_digit = False
for i in range(len(f)):
    
    if (f[i] in digits) == was_digit:
            len_podposled +=1
            mmax_len = max(mmax_len, len_podposled)

    else:
        len_podposled = 1   

        if f[i] in digits:
            was_digit = True
        else:
            was_digit = False
        
print(mmax_len)
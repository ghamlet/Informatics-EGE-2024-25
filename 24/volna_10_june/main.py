s = open("24.txt").readline()
for c in "24680":
    s = s.replace(c, "2")

mx = 0
for l in range(len(s)):
    for r in range(l+mx, len(s)):
        string = s[l:r+1]
        if string[0] not in "02468" or string.count("S") > 35 or string.count("2") >1:
            break

        if string.count("S") == 35:
            mx = max(mx, len(string))
            print(string)

print(mx)


#
# for c in "24680":
#     s = s.replace(c, "2")
#
# maxx = 0
# for i in range(len(s)):
#     for j in range(i + maxx, len(s)):
#         cut = s[i:j + 1]
#         if cut.count("S") > 35 or cut.count("2") > 1 or cut[0] != "2":
#             break
#         if cut.count("S") == 35:
#             maxx = max(maxx, len(cut))
# print(maxx)
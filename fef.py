n = "123153513"


dec = sum([int(s) * 8**i for i, s in enumerate(n[::-1])])
print(dec)
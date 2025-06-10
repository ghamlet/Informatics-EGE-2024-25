from string import printable

alp = printable[:27]

for x in alp:
    a = int(f"2107{x}792", 27) + int(f"565{x}211", 27)
    if a% 26==0:
        print(x, a//26)
        break
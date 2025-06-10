from string import  printable

alp = printable[:21]

for x in alp:
    a = int(f"82934{x}2", 21) + int(f"2924{x}{x}7", 21) + int(f"67564{x}8", 21)
    if a%20==0:
        print(x, a//20)
        break
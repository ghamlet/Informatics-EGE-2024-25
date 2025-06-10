f = open("9_21592.csv")
n = 1
for i in f:
    a = list(map(int, i.split(";")))
    # – в строке есть ровно три числа, каждое из которых повторяется дважды, остальные числа без повторений
    povt = [i for i in a if a.count(i) == 2]
    nepov = [i for i in a if a.count(i) == 1]

    sum_kv = 2 * sum(i ** 2 for i in nepov)

    if len(povt) == 6 and len(nepov) == 2:
        if (max(povt) - min(povt)) ** 2 > sum_kv:
            print(n)

    n += 1

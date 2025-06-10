def is_prime(n):
    if n ==1: return False
    for x in range(2, int(n**0.5)+1):
        if n%x ==0:
            return False
    return True


def find_deviders(n):
    d = []
    for x in range(1, int(n**0.5)+1):
        if n%x==0:
            # в список делителей добавляем сразу парами делители
            d.append([x, n//x])
    return d


def check_5(n):
    return str(n).count("5")==1


cnt = 0
for x  in range(1_324_728, 2_222_222):
    deviders = find_deviders(x)  # находим возможные пары чисел, произведение которых дает данное число
    for a,b in deviders:
        if is_prime(a) and is_prime(b) and check_5(a) and check_5(b):
            print(x, max(a,b))
            cnt+=1
            if cnt ==5:
                exit()


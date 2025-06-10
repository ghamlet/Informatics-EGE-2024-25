def f(start, end, c):
    if start > end: return  0

    if start == end: return  1

# Команда С может быть исполнена только после команды А
    if c == "A":
        return f(start+1, end, "A") + f(start+2, end, "B") + f(start*3, end, "C")
# иначе не используем команду С
    return  f(start+1, end, "A") + f(start+2, end, "B")


print(f(4, 16, 0))
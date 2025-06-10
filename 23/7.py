def f(start, end, s):
    if start > end +5 or 'AAAA' in s:
        return 0
    elif start == end and 'AAAA' not in s:
     return 1
    else:
        return f(start - 1, end, s + 'A') + f(start + 6, end, s + 'B') + f(start * 3, end, s + 'C')

print(f(7,35,''))



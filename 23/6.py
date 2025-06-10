def f(start, end, s):
    if start > end: return 0
    elif start == end and 'AAAA' not in s and 'BBBB' not in s:
        return 1
    else:
        return f(start + 1, end, s + 'A') + f(start * 2, end, s + 'B')

print(f(1, 402, ''))
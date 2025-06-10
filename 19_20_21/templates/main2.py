# Константин Поляков
# разбор https://www.youtube.com/watch?v=saqqoCS6wjk
# сайт для визуализации рекурсии https://recursion.vercel.app/

def f(s, m): #  s - количество камней, m - ходы в игре
    # условие завершения игры
    if s >= 88: return m % 2 == 0

    if m == 0: return 0      # если ходы в игре закончились

    # возможные ходы по условию, m-1 так делаем ход
    h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 3, m - 1)]

    # если номер хода нечетный, т. е. ходит Петя, то ему нужен любой ход для победы
    # !!! При первом неудачном ходе Пети нужно return any(h)
    return any(h) if m % 2 != 0 else all(h)


print('19)', [s for s in range(1, 88) if f(s, 2)])
print('20)', [s for s in range(1, 88) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 88) if not f(s, 2) and f(s, 4)])
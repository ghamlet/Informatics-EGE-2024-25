"""
№ 21604 (Уровень: Базовый)

(А. Левченко) У исполнителя имеются три команды, которые обозначены латинскими буквами:

A. Вычти 1
B. Вычти 4
C. Найди целую часть от деления на 2

Первая команда уменьшает число на экране на 1, вторая команда уменьшает это число на 4,
третья команда делит число нацело на 2. Программа для исполнителя – это последовательность команд.
Сколько существует таких программ, которые исходное число 34 преобразуют в число 9, при этом траектория вычислений содержит
числа 20 и 30, и не содержит числа 24?"""


def f(a,b):
    if a<b or a ==24: return 0  # когда происходит уменьшение числа а то знак меняется
    if a== b:
        return  1
    return f(a-1, b) + f(a-4, b) + f(a//2, b)

print(f(34, 30) * f(30, 20) * f(20, 9))
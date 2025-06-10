from turtle import *

f = open("demo_2025_27_Б__4v457.txt")
s = f.readline()

screensize(1000,1000)
tracer(0)
penup()
m = 40

# рисуем оси
for i in range(-50, 50):
    goto(i*m, 0); dot(4)
    goto(0, i*m); dot(4)

# рисуем точки
for line in f:
    line = line.replace(",", ".")
    x, y = map(float, line.split())
    goto(x*m, y*m); dot(4)

done()
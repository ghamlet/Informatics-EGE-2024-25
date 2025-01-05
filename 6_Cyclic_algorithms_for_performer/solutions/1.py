from turtle import *


#  её голова направлена вдоль положительного направления оси ординат, хвост опущен.
left(90)  # так как в питоне черепаха сначала смотрит направо по оси абцисс

tracer(0)   # speed(0)

screensize(10000, 10000)
k = 20


for i in range(8):
    forward( 16*k)
    right(90)
    forward(22*k)
    right(90)

penup()

forward(5*k)
right(90)
forward(5*k)
left(90)

pendown()

for i in range(8):
    forward(52*k)
    right(90)
    forward(77*k)
    right(90)


# перед рисованием сетки нужно поднять хвост
penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*k, y*k)
        dot(3, 'red')

update()    
done()
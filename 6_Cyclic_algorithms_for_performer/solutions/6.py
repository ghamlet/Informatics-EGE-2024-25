from turtle import *

tracer(0)
screensize(2222, 2222)
left(90)
k = 20

for i in range(9):
    forward(22*k)
    right(90)
    forward(6*k)
    right(90)

penup()

forward(1*k)
right(90)
forward(5*k)
left(90)

pendown()

for i in range(9):
    forward(53*k)
    right(90)
    forward(75*k)
    right(90)
    
penup()
for x in range(-22, 22):
    for y in range(-22, 22):
        goto(x*k, y*k)
        dot(3)
        
update()
done()
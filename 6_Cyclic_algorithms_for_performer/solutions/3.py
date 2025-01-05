from turtle import *

tracer(0)
screensize(2222, 2222)

k = 22
left(90)

for i in range(2):
    forward(24*k)
    right(90)
    forward(10*k)
    right(90)
    
penup()
forward(3*k)
left(90)
forward(13*k)
right(90)

pendown()
for i in range(2):
    forward(9*k)
    right(90)
    forward(32*k)
    right(90)
    
    
penup()

for x in range(-20, 22):
    for y in range(-22, 22):
        goto(x*k, y*k)
        dot(3)
        
update()
done()
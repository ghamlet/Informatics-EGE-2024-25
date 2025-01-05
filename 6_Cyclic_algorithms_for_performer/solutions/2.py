from turtle import *

tracer(0)
screensize(2222, 2222)
k = 20
left(90)

for i in range(13):
    forward(13 *k)
    right(90)
    forward(5*k)
    
penup()

right(90)
forward(7*k)
left(90)
forward(10*k)
pendown()

for i in range(23):
    forward(8*k)
    left(90)
    forward(11*k)
    left(90)
    
penup()
for x in range(33):
    for y in range(-10, 33):
        goto(x*k, y*k)
        dot(3)
        
update()
done()
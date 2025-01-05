from turtle import *

tracer(0)
screensize(2222, 2222)
left(90)
k = 20

for i in range(4):
    forward(16*k)
    left(90)
    forward(20*k)
    left(90)
    
penup()

forward(4*k)
left(90)
forward(8*k)
right(180)
pendown()

for i in range(3):
    forward(35*k)
    left(90)
    forward(6*k)
    left(90)
    
penup()
for x in range(-22, 31):
    for y in range(-22, 22):
        goto(x*k, y*k)
        dot(3)
        
update()
done()   


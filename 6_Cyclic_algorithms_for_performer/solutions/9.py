from turtle import *

screensize(2222, 2222)
left(90)
tracer(0)
m = 112


for i in range(13):
    right(135)
    forward(5*m)
    
up()
for x in range(-11, 11):
    for y in range(-11, 11):
        goto(x*m, y*m)
        dot(3)    
    
update()
done()


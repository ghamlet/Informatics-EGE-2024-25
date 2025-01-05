from turtle import *

tracer(0)
screensize(11111, 11111)
left(0)
k = 20

forward(25*k)
right(45)
forward(50*k)
penup()

back(50*k)
right(45)
forward(15*k)
left(90)
forward(30*k)
pendown()

right(180)
forward(60*k)
back(5*k)
right(90)
forward(31*k)

penup()
for x in range(-11,44):
    for y in range(-22,11):
        goto(x*k, y*k)
        dot(3)



update()
done()


print((25 +40)/2 *15)
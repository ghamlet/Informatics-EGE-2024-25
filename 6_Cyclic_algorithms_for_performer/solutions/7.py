from turtle import *

tracer(0)
screensize(4222, 4222)


left(90)
k = 5

right(45)

for i in range(70):
    right(45)
    forward(203*k)  #  203 - длина ,то точек внутри 202, а если включать границы то точек 204
    right(45)


penup()


back(40*k)
right(45)
pendown()

begin_fill()

for i in range(5):
    
    forward(20*k)
    left(90)
    
end_fill()

cnt = 0
canvas = getcanvas()    
for x in range(-222,222):
    for y in range(-222,222):
    
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (7,):  # (7,) точка заливки (внутри фигуры)
            cnt+=1
print(cnt)

update()

done()
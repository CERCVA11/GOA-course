from turtle import *


#we want to paint a house 

#step 1:  draw a square

from turtle import *


#we want to paint a house


#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)       #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200, 200)
begin_fill()
pendown()
color("grey")
right(150)
forward(200)
left(120)
forward(200)
end_fill()






#drawing a window
penup()
goto(60, 100)
pendown()



color("red") 
begin_fill()
left(30)
forward(60)
right(90)
forward(50)












































exitonclick()
from turtle import *

setup(1500,1000)

#we want to paint a house

#step 1: draw a squre
speed(2)

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward (200)
left(90)

forward (200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill ()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()
color("red")
begin_fill ()
right(150)
forward(200)
left (120)
forward(200)
end_fill()

#end 


# drawing a window
penup()
goto(20,150 )
pendown()
color("brown")
left(30)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)


width(3)
right(180)
forward(15)
right(90)
forward(40)
penup()
goto (20,130)
pendown()
left(90)
forward(30)

# end of drawing first window

width(7)
penup()
goto(180,150)
pendown()
left(180)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
width (3)
left(90)
forward(15)
left(90)
forward(40)
penup()
goto(180,130)
pendown()
right(90)
forward(30)

# end of drawing second window

penup()
goto(0,0)
pendown()

exitonclick()
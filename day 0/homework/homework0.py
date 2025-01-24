from turtle import *

width (7)
begin_fill()
color("brown")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()


forward(70)
begin_fill()
color("yellow")
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
begin_fill()
color("red")
right (150)
forward(200)

left(120)
forward(200)
end_fill()

penup()
goto(140, 115)
pendown()
begin_fill()
color("blue")
 
left (120)
forward(50)

right(90)
forward(40)

right(90)
forward(50)

right(90)
forward(40)
end_fill()

penup()
goto(60, 115)
pendown()

begin_fill()
color("blue")

left(90)
forward(50)

left(90)
forward(40)

left(90)
forward(50)

left(90)
forward(40)
end_fill()

exitonclick()
from turtle import *

# Set the drawing speed
speed(0)

# Set the background color to black to represent space
bgcolor("black")

# Draw the sun
color("orange")
begin_fill()
circle(60)
end_fill()

penup()
forward(100)
pendown()

# Draw the moon
color("grey")
begin_fill()
circle(20)
end_fill()

#move forward
penup()
forward(80)
pendown()

#create red planet
color("red")
begin_fill()
circle(40)
end_fill()

#move forward
penup()
forward(90)
pendown()

#green planet
color("green")
begin_fill()
circle(30)
end_fill()

#finish code
done()
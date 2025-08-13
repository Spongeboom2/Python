from turtle import *

def move_and_turn (distance, angle, color):
    """Move the turtle forward by 'distance' and turn it right by 'angle' degrees."""
    forward(distance)
    right(angle)
    fillcolor(color)

begin_fill()
move_and_turn(100, 90, "red")
move_and_turn(100, 90, "red")
move_and_turn(100, 90, "red")
move_and_turn(100, 90, "red")
end_fill()

penup()
forward(200)
pendown()

begin_fill()
move_and_turn(200, 90, "blue")
move_and_turn(200, 90, "blue")
move_and_turn(200, 90, "blue")
move_and_turn(200, 90, "blue")
end_fill()

penup()
left(90)
forward(100)
pendown()

begin_fill()
move_and_turn(150, 90, "green")
move_and_turn(150, 90, "green")
move_and_turn(150, 90, "green")
move_and_turn(150, 90, "green")
end_fill()

done()
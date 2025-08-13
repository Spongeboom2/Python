from turtle import *

def move_and_turn (distance, angle):
    """Move the turtle forward by 'distance' and turn it right by 'angle' degrees."""
    forward(distance)
    right(angle)

move_and_turn(100, 90)
move_and_turn(150, 30)
done()
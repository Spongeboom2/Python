from turtle import *

def move_and_turn(angle):
    forward(50)
    left(angle)


for i in range(8):
    move_and_turn(45)

done()
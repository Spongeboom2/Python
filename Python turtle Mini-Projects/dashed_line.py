from turtle import *

def move(distance):
    forward(distance)
    penup()
    forward(10)
    pendown()


for i in range(8):
    move(10)

done()
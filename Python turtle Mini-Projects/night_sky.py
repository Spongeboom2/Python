from turtle import *
from random import *

#set the background to black
bgcolor("black")

#Hide the turtle cursor
hideturtle()

#check width and height of the window
width = window_width()
print(width)
height = window_height()
print(height)

# Function to draw a star at a given position with a given size
def draw_star(x, y):
    size = randrange(4, 10)
    penup()
    goto(x, y)
    pendown()
    dot(20, "white")  # Draw the star as a white dot

for i in range(100):
    print("draw star")
    x = randrange(-width // 2, width //2)
    y = randrange(-height //2, height //2)
    draw_star(x, y)

#finishing the drawing
done() 

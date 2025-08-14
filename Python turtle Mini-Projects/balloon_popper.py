from turtle import *
from random import *

diameter = 40
pop_diameter = 100

#Draws a red balloon with the current diameter
def draw_balloon():
    color("red")
    #Draws a circle around the turtle
    dot(diameter)

#inflates the balloon by increasing the diameter by 10
def inflate_balloon():
    global diameter
    diameter = diameter + randint(5, 20)
    color(randint(0,255), randint(0,255), randint(0,255))
    draw_balloon()

def deflate_balloon():
    global diameter
    diameter = diameter - randint(5, 20)
    color(randint(0,255), randint(0,255), randint(0,255))
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!", align="center", font=("Arial", 24, "normal"))

#Initial drawing of the balloon
draw_balloon()

#When the up arrow key is pressed, inflate_balloon function is called
#The listen() function tells the program to start listening for events
onkey(inflate_balloon, "Up")
onkey(deflate_balloon, "Down")
listen()

done()

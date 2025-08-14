from turtle import *

#setup screen
speed(0)
move_distance = 50
bgcolor("#D2691E")

#go to starting position for drawing the water
penup()
goto(200, 450)
pendown()

#draw the water
begin_fill()
fillcolor("lightblue")
goto (500, 450)
goto(500,-450)
goto(200, -450)
goto(200, 450)
end_fill() 

#draw the turtle
penup()
goto(-200, 0)
shape("turtle")
color("green")

#movement functions
def move_up():
    setheading(90)
    forward(move_distance)
    check_win()

def move_down():
    setheading(270)
    forward(move_distance)
    check_win()

def move_left():
    setheading(180)
    forward(move_distance)
    check_win()

def move_right():
    setheading(0)
    forward(move_distance)
    check_win()

#check win function
def check_win():
    if xcor() > 200:
        #Win condition
        hideturtle()
        color("white")
        goto(0,0)
        write("You Win!", align="center", font=("Arial", 50, "normal"))

        #disable further movement
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")

#keyboard bindings
onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()

done()
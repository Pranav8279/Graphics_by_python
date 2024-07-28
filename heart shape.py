# import the turtle module

import turtle

#set up the screen and change the background color

screen=turtle.Screen()
screen.bgcolor("black")

# function to draw a balloon

def draw_balloon(t, x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.color('white')
    t.width(2)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.left(90)
    t.width(1)

# position of the heart


heart_x,heart_y=0,0

#draw the heart shape


t=turtle.Turtle()
s=turtle.Turtle()


t.hideturtle()
t.goto(heart_x,heart_y-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

#move the centre of heart to write the text

t.penup()

t.goto(heart_x,heart_y)
t.pendown()
t.color('white')
t.write(" love you",align="center",font=("verdana",25,"bold"))

# draw the balloons at your position

balloons = turtle.Turtle()
balloons.hideturtle()
draw_balloon(balloons, -200, 200, 'blue')
draw_balloon(balloons, 200, 200, 'yellow')
draw_balloon(balloons, -200, -200, 'green')
draw_balloon(balloons,200,-200,'light blue' )

# open the window

turtle.done()
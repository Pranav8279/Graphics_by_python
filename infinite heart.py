# import the maths and turtle modules
import math
from turtle import *

# define a function to create the x coordinate of the heart shape

def heart(k):
    return 15*math.sin(k)

# define a function to create the y coordinate of the heart shape

def heart1(k):
    return 12*math.cos(k)-5*\
       math.cos(2*k)-2*\
       math.cos(3*k)-\
       math.cos(4*k)

# create a new turtle screen and set its background color

speed(1000)
bgcolor('black')

#loop to draw the heart shape

for i in range(6000):
    goto(heart(i)*20,heart1(i)*20)
    # loop to set the color of heart shape
    for j in range(5):
        color('pink')

#finish the drawing

done()
    
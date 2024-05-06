import turtle
from turtle import Turtle, Screen
import random


tim=Turtle()
#tim.shape('turtle')
turtle.colormode(255) 
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors=(r,g,b)
    return colors

tim.pensize(10)
tim.speed(10)
colors=()
for j in range(300):
    tim.color(random_color())
    
    tim.forward(30)
    
    tim.setheading(90*random.randint(1,4))







 








screen= Screen()
screen.exitonclick()


# for i in range(4):
#     for i in range(10):
#         tim.forward(10)
#         tim.color('white')
#         tim.forward(10)
#         tim.color('black')

#     tim.right(90)
# for i in range(4):
#     for i in range(10):
#         tim.forward(10)
#         tim.pendown()
#         tim.forward(10)
#         tim.penup()

#     tim.right(90)

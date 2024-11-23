#დახაზე სახლლი def და for ის დახმარებით 
from turtle import *
#draw a square
def square():
    for i in range(4):
        forward(200)
        left(90)

#we want to paint a house

#step 1: draw a square
color("purple")
width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
                 
forward(200)
left(90)
#end of square


#drawing a door
forward(70)   
color("yellow")   
left(90)               
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
speed(40)
penup()
goto(200,200)
pendown()


#drawing a roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)



exitonclick()
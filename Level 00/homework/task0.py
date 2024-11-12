from turtle import *

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
right(150)
forward(200)
left(120)
end_fill()

exitonclick()


exitonclick()
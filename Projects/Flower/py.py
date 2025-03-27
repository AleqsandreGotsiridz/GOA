from turtle import *

speed(0)
bgcolor("black")

for i in range(100):
    color("red")
    forward(8)
    circle(290 - i, 90)
    left(90)
    circle(290 - i, 90)
    left(28)

done()
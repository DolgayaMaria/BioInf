# from turtle import *
import turtle
a=turtle.Turtle()
b=turtle.Turtle()
a.speed(speed=0)
b.speed(speed=0)

a.color('red', 'yellow')
b.color('green','blue')
b.begin_fill()
a.begin_fill()
fill_a=True
fill_b=True
while True:
    if fill_a==True:
        a.forward(200)
        a.left(120)
    if fill_b==True:
        b.backward(200)
        b.right(60)

    print(a.pos(), " - ", b.pos())

    if (abs(a.pos()) < 1):
        fill_a=False
    if (abs(b.pos()) < 1):
        fill_b=False
    if (fill_a==False) and (fill_b==False):
        break
a.end_fill()
b.end_fill()


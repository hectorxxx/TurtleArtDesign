import turtle
from helper import *
import math
import random
from helper import*
#turtle.tracer(0)
turtle.colormode(255)
bob = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')
bob.speed(0)
bob.color('magenta')
rotate=int(360)

def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):

  for i in range (repeat):

    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(bob,100,10)

for times in range(50):
    bob.left(40)
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    hexogon(bob, 6, times*5, "red")

for times in range(50):
    bob.left(65)
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    hexogon(bob, 5, times*5, "cyan")

for times in range(100):
    r=random.randint(0,255) 
    g=random.randint(0,255)
    b=random.randint(0,255)
    myColor=(r,g,b)
    mySize=(times*0.2)
    mySide=random.randint(5,10)
    bob.penup()
    polygon(bob,mySide,mySize,myColor)
    bob.forward(times*0.5)
    bob.left(30)
    bob.pendown()




    


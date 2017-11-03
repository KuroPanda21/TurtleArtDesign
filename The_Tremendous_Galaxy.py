import turtle
from DesignFunctions import *
from random import *
turtle.colormode(255)
turtle.bgcolor(0,0,0)
bob=turtle.Turtle()
bob.speed(0)

for times in range(100):
    x = randint(-700,700) #random values for x and y
    y = randint(-400,400)
    
    dist = randint(5,20) #gives random values for lines from center

    bob.color(255,255,255) #white

    jump(bob,x,y)   
    star(bob,dist)      #draw stars and connect it to the origin
    bob.home()

dist = 50
r = 0
g = 255
b = 255
bob.left(45)
for times in range(255):    #creates pattern(5 squares) that change color
    bob.color(r,g,b)
    polygon(bob,dist,4)
    bob.left(144)
    dist = dist+1
    g = g-1
    r = r+1
    
for times in range(10):
    x = randint(-600,600) #random values for x and y
    y = randint(-400,400)
    
    red = randint(100,255) #random colors
    green = randint(100,255)
    blue = randint(100,255)
    bob.color(red,green,blue)
   
    jump(bob,x,y)

    for times in range(1):      #creates colorful planets
        for planet in range(190):
            bob.color(red,green,blue)
            bob.forward(planet)
            bob.left(planet)


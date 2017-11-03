#define the fn polygon
# that takes in a turtle, a side length
# and number of sides
def polygon(t,dist,sides):
    angle=360/sides
#    t.begin_fill()
    for times in range(sides):
        t.forward(dist)
        t.left(angle)
#    t.end_fill()

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def star(t,d):
    for times in range(5):
        t.left(144)
        t.forward(d)




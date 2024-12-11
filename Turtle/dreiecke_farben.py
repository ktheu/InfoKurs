from turtle import *

def dreieck(laenge,bremse):
    if bremse == 0: return
    
    left(90)
    color(farben[bremse%len(farben)])
    fd(laenge//2)

    for i in range(3):
        pos = position()
        head = heading()
        
        left(30)
        dreieck(0.45*laenge,bremse-1)
        
        setpos(pos)
        setheading(head)
        right(120)
        
        color(farben[bremse%len(farben)])
        if i == 2:
            fd(laenge//2)
        else:
            fd(laenge)
  
farben = ['red','green','blue','orange','yellow']  
hideturtle()
speed(0)
up()
goto(0,-100)
down()
left(90)
pensize(2)
dreieck(200,4)
from turtle import *

def dreieck(laenge,bremse):
    if bremse == 0: return
    
    left(90)
    fd(laenge//2)

    for i in range(3):
        pos = position()
        head = heading()
        
        left(30)
        dreieck(0.45*laenge,bremse-1)
        
        setpos(pos)
        setheading(head)
        right(120)

        if i == 2:
            fd(laenge//2)
        else:
            fd(laenge)
  
    
hideturtle()
speed(0)
up()
goto(0,-100)
down()
left(90)
dreieck(200,4)
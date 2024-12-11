from turtle import *
    
def zeichne(laenge,bremse):
    if bremse == 0: 
        down()
        forward(laenge)
        up()
        return
    
    zeichne(laenge//3,bremse-1)
    left(60)
    zeichne(laenge//3,bremse-1)
    right(120)
    zeichne(laenge//3,bremse-1)
    left(60)
    zeichne(laenge//3,bremse-1)

#hideturtle()
speed(4)
up()
goto(-200,0)
zeichne(400,3)


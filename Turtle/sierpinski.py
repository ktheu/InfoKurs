from turtle import *
    
def zeichne(laenge,bremse):
    
    if bremse == 0:
        down()
        for i in range(3):    # Dreieck zeichnen
            forward(laenge)
            left(120)
        up()
        return
    
    pos = position()
    winkel = heading()
    
    zeichne(laenge//2,bremse-1)    # 1. Dreieck links unten
    
    forward(laenge//2)
    zeichne(laenge//2,bremse-1)    # 2. Dreieck rechts unten
    
    left(120)
    forward(laenge//2)
    right(120)
    
    zeichne(laenge//2,bremse-1)
    
    setpos(pos)
    setheading(winkel)

speed(4)
#hideturtle()
up()
goto(-320,-280)
zeichne(650,2)


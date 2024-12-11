from turtle import *
    
def zeichne(laenge,bremse):
    global zaehl
    zaehl+=1
    write(zaehl)
    if bremse == 0:
        dot(8,'green')
        return
    dot(8,'red')
    
    # Ausgangsposition merken
    pos = position()
    winkel = heading()
    
    
    # 1. Verzweigung
    right(40)
    forward(laenge)
    zeichne(laenge*0.7,bremse-1)
    
    # zurück auf Ausgangsposition
    up()
    setpos(pos)
    setheading(winkel)
    down()
  
    
    # 2. Verzweigung
    left(40)
    forward(laenge)
    zeichne(laenge*0.7,bremse-1)
    
     
    
hideturtle()
zaehl = 0
pensize(1)
speed(0)
up()
goto(0,-200)
down()
left(90)
zeichne(150,3)
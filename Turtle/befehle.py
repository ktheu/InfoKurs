from turtle import *
farben = ['red','green','blue','orange']
        
    
def zeichne(laenge,bremse):
    if bremse == 0:
        return
    
    # Ausgangsposition merken
    pos = position()
    winkel = heading()
    
    # 1. Verzweigung
    right(45)
    color(farben[bremse%len(farben)])
    forward(laenge)
    zeichne(laenge*0.5,bremse-1)
    
    # zurück auf Ausgangsposition
    up()
    setpos(pos)
    setheading(winkel)
    down()
    
    # 2. Verzweigung
    left(45)
    color(farben[bremse%len(farben)])
    forward(laenge)
    zeichne(laenge*0.5,bremse-1)
    
hideturtle()

up()
down()
pensize(3)
speed(10)
left(90)
zeichne(200,4)
mainloop()
 
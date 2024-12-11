from turtle import *
farben = ['red','green','blue','orange']
        
    
def zeichne(laenge,bremse):
    if bremse == 0:
        dot(5)
        return
    
    # Ausgangsposition merken
    pos = position()
    winkel = heading()
    
    # 1. Verzweigung
    right(90)
    down()
    color(farben[bremse%len(farben)])
    forward(laenge)
 
    right(30)
    forward(laenge*0.6)
    left(90)
    forward(laenge*0.4)
    up()
    zeichne(laenge*0.5,bremse-1)
    
    setpos(pos)
    setheading(winkel)
    left(45)
        # 1. Verzweigung
 
    down()
    color(farben[bremse%len(farben)])
    forward(laenge)
 
    right(70)
    forward(laenge*0.6)
    up()
    zeichne(laenge*0.5,bremse-1)
    
    setpos(pos)
    setheading(winkel)
    left(120)
        # 1. Verzweigung
 
    down()
    color(farben[bremse%len(farben)])
    forward(laenge)
 
    left(30)
    forward(laenge*0.6)
    up()
    zeichne(laenge*0.5,bremse-1)


    
hideturtle()

up()
down()
pensize(2)
tracer(0,0)
left(90)
zeichne(160,5)
mainloop()
 

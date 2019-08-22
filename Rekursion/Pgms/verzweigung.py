import turtle as t
    
def zeichne(laenge,bremse):
    if bremse == 0:
       return
    
    # Ausgangsposition merken
    pos = t.position()
    winkel = t.heading()
    
    # 1. Verzweigung
    t.right(45)
    t.forward(laenge)
    zeichne(laenge*0.5,bremse-1)
    
    # zurück auf Ausgangsposition
    t.penup()
    t.setpos(pos)
    t.setheading(winkel)
    t.pendown()
    
    # 2. Verzweigung
    t.left(45)
    t.forward(laenge)
    zeichne(laenge*0.5,bremse-1)
    
t.hideturtle()
t.left(90)
t.speed(10)
zeichne(200,6)

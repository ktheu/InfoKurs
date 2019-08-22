import turtle as t
    
def zeichne(laenge,bremse):
    if bremse == 0: 
        t.dot(10, "red")
        return
    
    # Ausgangsposition merken
    pos = t.position()
    winkel = t.heading()
    
    # rechter Ast
    t.right(60)
    t.forward(laenge)
    zeichne(laenge * 0.7, bremse-1)
    
    # zurück auf Ausgangsposition
    t.penup()
    t.setpos(pos)
    t.setheading(winkel)
    t.pendown()
    
    # linker Ast
    t.left(40)
    t.forward(laenge * 0.8)
    zeichne(laenge * 0.6, bremse-1)


t.speed(10)
t.hideturtle()
 
t.penup()
t.setpos(-50,-300)       # Startposition
t.setheading(90)

t.pendown()
t.forward(200)           # Stamm zeichnen
zeichne(200,6)


import turtle as t

def leftmouse(x,y):
    global bremse
    bremse += 1
    baum()
    
def rightmouse(x,y):
    global bremse
    if bremse > 0:
        bremse -= 1
    baum()
    
def zeichne(laenge,bremse):
    if bremse == 0: return
    
    t.forward(laenge*0.5) # am Stamm entlang gehen
    
    pos = t.position()    # Position 1 merken
    winkel = t.heading()
    
    t.right(40)           # rechter Ast
    zeichne(laenge*0.7,bremse-1)
    
    t.penup()             # zurück auf Position 1
    t.setpos(pos)
    t.setheading(winkel)
    
    t.pendown()           # am Stamm etwas weiter gehen
    t.forward(laenge*0.3)
    
    pos = t.position()    # Position 2 merken
    winkel = t.heading()
    
    t.left(60)            # linker Ast
    zeichne(laenge*0.5,bremse-1)
    
    t.penup()             # zurück auf Position 2
    t.setpos(pos)
    t.setheading(winkel)
    
    t.pendown()           
    t.forward(laenge*0.2) # Stamm fertig zeichnen 


def baum():
    t.reset()
    t.hideturtle()
    t.color('green')
    
    t.penup()             # Ausgangsposition
    t.setpos(-50,-300)
    t.setheading(90)
    
    t.pendown()           # Aufruf der rekursiven Funktion
    zeichne(400,bremse)
    t.update()            # Bild zeigen
    
t.tracer(0,0)
t.onscreenclick(leftmouse,btn=1)
t.onscreenclick(rightmouse,btn=3)
bremse = 2               # Rekursionsstufen
baum()

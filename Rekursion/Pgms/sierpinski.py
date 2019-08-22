import turtle as t

def leftmouse(x,y):
    global bremse
    bremse += 1
    sierpinski()
    
def rightmouse(x,y):
    global bremse
    if bremse > 0:
        bremse -= 1
    sierpinski()
    
def zeichne(laenge,bremse):
    if bremse == 0: 
        t.pendown()       
        for i in range(3):    # Dreieck zeichnen
            t.forward(laenge)
            t.left(120)
        t.penup()
        return
    
    halb = laenge/2
    
    zeichne(halb,bremse-1)    # 1. Dreieck links unten
    
    t.forward(halb)
    
    zeichne(halb,bremse-1)    # 2. Dreieck rechts unten
    
    t.left(120)
    t.forward(halb)
    t.right(120)
    
    zeichne(halb,bremse-1)    # 3. Dreieck oben
    
    t.right(120)              # zurück in die Ausgangsposition
    t.forward(halb)
    t.left(120)

def sierpinski():
    t.reset()
    t.hideturtle()
    
    t.penup()              # Ausgangsposition
    t.setpos(-350,-280)
    t.setheading(0)
    
    zeichne(650,bremse)    # Aufruf der rekursiven Funktion
    t.update()             # Bild zeigen


t.tracer(0,0) 
t.onscreenclick(leftmouse,btn=1)
t.onscreenclick(rightmouse,btn=3)

bremse = 2
sierpinski()

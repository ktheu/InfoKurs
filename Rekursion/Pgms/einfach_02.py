import turtle as t

def zeichne(laenge,bremse):
    if bremse == 0: return
    t.fd(laenge)
    pos = t.position()
    
    # speichere Zustand vor der Rekursion 
    winkel = t.heading()
 
    
    t.left(40)
    zeichne(laenge * 0.7,bremse-1)
    
    t.up()
    t.setpos(pos)
    t.setheading(winkel)
    t.down()
    
    t.right(40)
    zeichne(laenge * 0.5,bremse-1)
    
    
t.speed(0)
bremse = 8
t.up()
t.goto(0,-300)
t.left(90)
t.down()
zeichne(200,bremse)
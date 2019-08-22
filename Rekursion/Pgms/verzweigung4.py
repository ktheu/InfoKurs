import turtle as t
    
def zeichne(laenge,bremse):
    if bremse == 0: 
       return
    pos = t.position()
    winkel = t.heading()
    t.right(45)
    t.forward(laenge)
    zeichne(laenge*0.5,bremse-1)
    
    t.penup()
    t.setpos(pos)
    t.setheading(winkel)
    t.pendown()
    t.left(45)
    t.forward(laenge)
    zeichne(laenge*0.5,bremse-1)
    
    t.penup()
    t.setpos(pos)
    t.setheading(winkel)
    t.pendown()
    t.left(135)
    t.forward(laenge)
    zeichne(laenge*0.5,bremse-1)
    
    t.penup()
    t.setpos(pos)
    t.setheading(winkel)
    t.pendown()
    t.right(135)
    t.forward(laenge)
    zeichne(laenge*0.5,bremse-1)

#t.tracer(0,0)

t.ht()
t.left(90)
t.tracer(0,0)
zeichne(200,4)

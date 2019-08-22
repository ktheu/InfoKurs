import turtle as t

def leftmouse(x,y):
    global bremse
    bremse += 1
    koch()
    
def rightmouse(x,y):
    global bremse
    if bremse > 0:
        bremse -= 1
    koch()
    
def zeichne(laenge,bremse):
    if bremse == 0: 
        t.pendown()
        t.forward(laenge)
        t.penup()
        return
    
    drittel = laenge/3   
    
    zeichne(drittel,bremse-1)
    t.left(60)
    zeichne(drittel,bremse-1)
    t.right(120)
    zeichne(drittel,bremse-1)
    t.left(60)
    zeichne(drittel,bremse-1)
    
def koch():
    t.reset()
    t.hideturtle()
    
    t.penup()             # Ausgangsposition
    t.setpos(-380,180)
    t.setheading(0)
    
    for i in range(3):    # 3 Seiten der Schneeflocke
        zeichne(650,bremse)
        t.right(120)
    t.update()
    
t.tracer(0,0)       
t.onscreenclick(leftmouse,btn=1)
t.onscreenclick(rightmouse,btn=3)

bremse = 2
koch()

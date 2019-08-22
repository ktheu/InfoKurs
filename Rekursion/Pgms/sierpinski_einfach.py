import turtle as t

def zeichne(laenge,bremse):
    
    if bremse == 0:
        t.down()
        for i in range(3):
            t.fd(laenge)
            t.left(120)
        t.up()
        return
    
    zeichne(laenge/2,bremse-1)
    
    t.fd(laenge/2)
    
    zeichne(laenge/2,bremse-1)
     
    t.left(120)
    t.fd(laenge/2)
    t.right(120)
    zeichne(laenge/2,bremse-1)
    
    t.right(120)
    t.fd(laenge/2)
    t.left(120)
    
bremse = 5
t.up()
t.goto(-300,-300)
t.speed(0) 
zeichne(600,bremse)
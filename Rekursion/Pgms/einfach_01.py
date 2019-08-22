import turtle as t

def zeichne(laenge,bremse):
    if bremse == 0: return
    t.fd(laenge)
    t.left(40)
    zeichne(laenge * 0.7,bremse-1)

bremse = 5
t.up()
t.goto(0,-300)
t.left(90)
t.down()
zeichne(200,bremse)
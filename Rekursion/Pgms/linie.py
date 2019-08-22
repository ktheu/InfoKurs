import turtle as t
    
def zeichne(laenge):
    if laenge < 5:
        return
    t.fd(laenge)
    t.up()
    t.fd(laenge*0.8)
    t.down()
    zeichne(laenge*0.8)

t.up()
t.goto(-400,0);
t.down()
t.pensize(5);
t.hideturtle()
zeichne(100)

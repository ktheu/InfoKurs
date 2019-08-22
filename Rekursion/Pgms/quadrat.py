import turtle as t
    
def zeichne(laenge):
    if laenge < 20:
        return
    t.fd(laenge)
    t.left(90)
    zeichne(laenge*0.98)

t.up()
t.goto(-350,-350);
t.down()
t.pensize(1);
t.hideturtle()
t.speed(10)
zeichne(700)

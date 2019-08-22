import turtle as t
    
def zeichne(laenge):
    if laenge < 20:
        return
    t.fd(laenge)
    t.left(60)
    zeichne(laenge*0.99)

t.up()
t.goto(-200,-350);
t.down()
t.pensize(1);
t.hideturtle()
t.speed(10)
zeichne(400)

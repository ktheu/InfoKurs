from turtle import Turtle, Screen  


def inMandel(x,y,k):
    '''
    x, y: floats
    k: ganze Zahl >= 0
    returns: True, wenn für c = x + iy das k-te Element der Folge
       0, c, c^2 + c, (c^2 + c)^2 + c, ... einen Betrag < 2 hat.
    '''
    c = x + 1j*y
    z = 0
    zaehl = 0
    while abs(z) < 2 and zaehl < k:
        z = z * z + c
        zaehl+=1
    if abs(z) < 2: return True
    return False

screen = Screen()
screen.tracer(0,0)

t = Turtle()
t.hideturtle()

iterationen = 10
schritt = 0.005
x = -2.0
while x < 0.45:     # -2.0 <= x <= 0.45
    x+=schritt
    y = 1.2
    while y > -1.2: # 1.2 >= y >= -1.2
        y-=schritt
        if inMandel(x,y,iterationen):
            t.penup()
            t.goto(200*x,200*y)
            t.pendown()
            t.dot(3,'black') 
screen.update()             
screen.mainloop()

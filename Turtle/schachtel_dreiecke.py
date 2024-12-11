from turtle import *

def dreieck(laenge,bremse):
    if bremse == 0: return
    
    for i in range(3):
        fd(laenge)
        left(120)
        
    up()
    left(60)
    fd(laenge//2)
    right(120)
    down()
    dreieck(laenge//2,bremse-1)

hideturtle()
speed(0)
up()
goto(-200,-200)
down()
 
pensize(1)
dreieck(400,6)
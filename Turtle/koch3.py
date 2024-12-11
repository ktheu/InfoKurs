from turtle import *
    
def zeichne(laenge,bremse):
    if bremse == 0: 
        down()
        forward(laenge)
        up()
        return
    
    zeichne(laenge//3,bremse-1)
    left(60)
    zeichne(laenge//3,bremse-1)
    right(120)
    zeichne(laenge//3,bremse-1)
    left(60)
    zeichne(laenge//3,bremse-1)

 
speed(0)
up()
goto(-300,150)

for i in range(3):    # 3 Seiten der Schneeflocke
    zeichne(500,3)
    right(120)
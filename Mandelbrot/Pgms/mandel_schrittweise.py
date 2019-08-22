'''
Die beiden Kreise haben Radius 1 und 2.

Ablauf:
(1) linksClick mit Maus für Startpunkt c (rot). Auch z wird
gleich auf c gesetzt.
(2) q - quadriert diesen Punkt (grün)
(3) a - addiert zum quadrierten Punkt c (z^2 + c) (blau)
(4) n - nur noch c und der letzte blaue Punkt
(5) q - quadriert den letzten blauen Punkt
(6) a - addiert zum quadrierten Punkt c (z^2 + c) (blau)
(7) n - nur noch c und der letzte blaue Punkt
usw. 

Es werden keine Fehler abgefangen.
'''

from turtle import Turtle, Screen
import math
t = Turtle()
t.hideturtle()
screen = Screen()

def drawAxisAndCirlce():
    screen.tracer(0,0)
    width = screen.window_width()
    height = screen.window_height()
    t.pencolor('black')
    t.up()
    t.home()
    t.down()
    t.dot(10)
    
    t.up()
    t.goto(0,-200)
    t.down()
    t.circle(200)
    
    t.up()
    t.home()
    t.goto(0,-100)
    t.down()
    t.circle(100)

    t.up()
    t.goto(-width//2,0)
    t.down()
    t.fd(width)

    t.up()
    t.goto(0,height//2)
    t.down()
    t.right(90)
    t.fd(height)
    screen.update()

def drawRedPoint(x,y):
    global c, z
    c = x/100 + 1j * y/100
    drawPoint(x,y,'red')
    z = c
    
def quadriere():
    global z
    z = z*z
    drawComplex(z,'green')
    
def addiere():
    global z
    tmp = z
    z = z + c
    drawComplex(z,'blue')
    drawline(tmp,z,'red')
    drawline(z,c,'green')

def neu():
    t.clear()
    drawAxisAndCirlce()
    drawComplex(c,'red')
    drawComplex(z,'blue')


def setC():
    global c, z
    x = screen.numinput("","Realteil")
    y = screen.numinput("","Imaginärteil")
    c = x + 1j * y
    z = c
    drawRedPoint(x*100,y*100)
    screen.listen()
    
def reset_():
    t.clear()
    drawAxisAndCirlce()
    
def drawComplex(z,farbe):
    drawPoint(z.real*100, z.imag*100, farbe)
    
def drawPoint(x,y,farbe):
    t.pencolor(farbe)
    t.up()
    t.home()
    t.down()
    t.goto(x,y)
    t.down()
    t.dot(10)
    koord = '('+str(round(x/100,2)) + '/' + str(round(y/100,2)) + ')'
    laenge = round(math.sqrt(x/100*x/100 + y/100 * y/100),2)
    #t.write(koord + ', Länge=' + str(laenge))
    screen.update()

def drawline(z1,z2,farbe):
    t.pencolor(farbe)
    t.up()
    t.goto(z1.real*100,z1.imag*100)
    t.down()
    t.goto(z2.real*100,z2.imag*100)
    screen.update()
    
drawAxisAndCirlce()
screen.listen()
screen.onscreenclick(drawRedPoint,btn=1)
screen.onkey(quadriere,'q')
screen.onkey(addiere,'a')
screen.onkey(reset_,'r')
screen.onkey(neu,'n')
screen.onkey(setC,'s')



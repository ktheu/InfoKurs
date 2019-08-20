############################################################
# IMPORTS
############################################################
from Baum import Baum
from Schlange import Schlange
import pygame
import random

############################################################
# GLOBALE VARIABELN
############################################################
SIGMA_TEILER = 6
GROESSE = [400, 400]

INORD = []
PREORD = []
POSTORD = []
BREIT = []


############################################################
# FUNKTIONEN
############################################################
def inorder(b):
    global INORD
    if b.empty(): return
    inorder(b.left())
    INORD.append(b.value())
    inorder(b.right())


def preorder(b):
    global PREORD
    if b.empty(): return
    PREORD.append(b.value())
    preorder(b.left())
    preorder(b.right())


def postorder(b):
    global POSTORD
    if b.empty(): return
    postorder(b.left())
    postorder(b.right())
    POSTORD.append(b.value())


def breitensuche(baum):
    global BREIT
    s = Schlange()
    if not baum.empty():
        s.enq(baum)
    while not s.empty():
        b = s.front()
        s.deq()
        BREIT.append(b.value())
        if not b.left().empty():
            s.enq(b.left())
        if not b.right().empty():
            s.enq(b.right())


def meinRandom(lower, upper):
    dif = upper - lower
    ans = round(random.gauss(dif / 2 + lower, dif / SIGMA_TEILER))
    while not (lower <= ans <= upper):
        ans = round(random.gauss(dif / 2 + lower, dif / SIGMA_TEILER))
    return ans


def BaumErzeugen(pos1, pos2):
    if pos2[0] - pos1[0] < 40 or pos2[1] - pos1[1] < 40: return Baum(Viereck(pos1, pos2))
    breite = pos2[0] - pos1[0]
    hoehe = pos2[1] - pos1[1]
    if breite > hoehe:
        breite1 = meinRandom(20, breite - 20)
        breite2 = breite - breite1
        pos1_1 = [pos1[0] + 5, pos1[1] + 5]
        pos1_2 = [pos1[0] + breite1 + 5, pos1[1] + 5]
        pos2_1 = [pos2[0] - breite2 - 5, pos2[1] - 5]
        pos2_2 = [pos2[0] - 5, pos2[1] - 5]
    else:
        hoehe1 = meinRandom(20, hoehe - 20)
        hoehe2 = hoehe - hoehe1
        pos1_1 = [pos1[0] + 5, pos1[1] + 5]
        pos2_1 = [pos2[0] - 5, pos2[1] - hoehe2 - 5]
        pos1_2 = [pos1[0] + 5, pos1[1] + hoehe1 + 5]
        pos2_2 = [pos2[0] - 5, pos2[1] - 5]
    return Baum(Viereck(pos1, pos2), BaumErzeugen(pos1_1, pos2_1), BaumErzeugen(pos1_2, pos2_2))


############################################################
# KLASSEN
############################################################
class Viereck():
    COLOURS = [[0, 0, 255], [0, 255, 0], [255, 0, 0], [255, 165, 0], [255, 192, 203],
                  [170, 170, 170],[255,255,0],[128,0,128],[255,0,255]]

    def __init__(self, pos1, pos2):
        self.x = pos1[0]
        self.y = pos1[1]
        self.breite = pos2[0] - pos1[0]
        self.hoehe = pos2[1] - pos1[1]
        self.colour = random.choice(Viereck.COLOURS)

    def draw(self, screen, offset):
        pygame.draw.rect(screen, self.colour, (self.x + offset[0], self.y + offset[1], self.breite, self.hoehe), 1)


############################################################
# INIT
############################################################
a = Viereck([10, 10], [100, 300])
pygame.init()
screen = pygame.display.set_mode((GROESSE[0] * 2 + 10, GROESSE[1] * 2 + 10))
b = BaumErzeugen([10, 10], GROESSE)
inorder(b)
preorder(b)
postorder(b)
breitensuche(b)
for each in range(len(INORD)):
    INORD[each].draw(screen, [0, 0])
    PREORD[each].draw(screen, [GROESSE[0], 0])
    POSTORD[each].draw(screen, [0, GROESSE[1]])
    BREIT[each].draw(screen, GROESSE)
    pygame.display.flip()
    pygame.time.wait(1000)
pygame.display.flip()

############################################################
# MAIN
############################################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit(0)

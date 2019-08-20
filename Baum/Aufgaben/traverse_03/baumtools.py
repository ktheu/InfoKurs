import pygame

def baumDarstellen(baum):
    layer = findeTiefe(baum) - 1
    drawBaum(baum, 30, layer)
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                end = True


def drawBaum(baum, sgroeße, layer):
    pygame.init()
    font = pygame.font.SysFont('Arial', sgroeße)
    screen = pygame.display.set_mode([(2 ** layer) * sgroeße * 2 + sgroeße, layer * 2 * sgroeße + 3 * sgroeße])
    screen.fill([255, 255, 255])
    recursiveDraw(screen, font, baum, [2 ** layer * sgroeße, sgroeße], sgroeße, layer, 0)
    pygame.display.flip()


def recursiveDraw(screen, font, baum, pos, sgroeße, maxlayer, layer):
    if baum.empty(): return False
    num = str(baum.value())
    numrender = font.render(num, False, [0, 0, 0])
    x = pos[0]
    y = pos[1]
    newX1 = x + sgroeße * 2 ** (maxlayer - (layer + 1))
    newX2 = x - sgroeße * 2 ** (maxlayer - (layer + 1))
    newY = y + 2 * sgroeße
    newpos1 = [newX1, newY]
    newpos2 = [newX2, newY]
    if len(num) == 2:
        screen.blit(numrender, pos)

    elif len(num) == 1:
        # x += sgroeße/2
        screen.blit(numrender, [x + sgroeße / 4, y])
        x += sgroeße / 4
    num1 = recursiveDraw(screen, font, baum.left(), newpos2, sgroeße, maxlayer, layer + 1)
    if num1 == 2:
        pygame.draw.line(screen, [0, 0, 0], [x, y + sgroeße], [newX2 + sgroeße / 2, newY])
    elif num1 == 1:
        pygame.draw.line(screen, [0, 0, 0], [x, y + sgroeße], [newX2 + sgroeße / 2, newY])
    if len(num) == 2:
        x += sgroeße / 2
    if recursiveDraw(screen, font, baum.right(), newpos1, sgroeße, maxlayer, layer + 1):
        pygame.draw.line(screen, [0, 0, 0], [x + sgroeße / 2, y + sgroeße], [newX1 + sgroeße / 2, newY])
    return len(num)

def findeTiefe(baum):
    '''
    Gibt die Toefe des Bauems zurück gezählt ab 1
    :param baum: Baum
    :return: int
    '''
    if baum.empty(): return 0
    return max(findeTiefe(baum.left()), findeTiefe(baum.right())) + 1

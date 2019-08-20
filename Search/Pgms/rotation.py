# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:49:28 2017
########
#     0#
#     0#
#112222#
#33   4#
#55   4#
#666  4#
### ####

n = 8
(0,1,6,2,True)
(1,3,1,2,False)  die 1 beginnt ab (3,1) hat länge 2, horizontal (=False)
(2,3,3,4,False)
(3,4,1,2,False)
(5,5,1,2,False)
(6,6,1,3,False)
(4,4,6,3,True)
(x,7,3,1,True)  # der Ausgang

"""
N = 8         # die Größe des Spielfeldes
def readinput(nr):
    global N
    '''
    nr: int, liest die Datei rotation<nr>-03.txt
    returns: NxN Belegungsmatrix
    '''
    f = open('rotation'+str(nr)+'_03.txt')
    data = []
    for zeile in f:
        data.append(list(zeile.strip()))
    f.close()
    N = data.pop(0)[0]    # die Größenzahl
    
    return data

def showMatrix(m):
    '''
    m: state-Tupel 
    n: int, Größe des Quadrats
    '''
    mx = [['.'] * N for i in range(N)]
   
    for e in m:
        zahl,x0,y0,laenge,richt = e
        x, y = x0, y0
        for k in range(laenge):
            mx[x][y] = zahl
            if richt:
                x+=1
            else:
                y+=1
        
    for z in mx:
        print(*z)
    print('-----')


def linksR(m):
    m = links(m)
    m1 = rutschen(m,leer(m))    
    while m != m1:
        m = m1[:]
        m1 = rutschen(m,leer(m))    
    #showMatrix(m)
    return tuple(m)

def rechtsR(m):
    m = rechts(m)
    m1 = rutschen(m,leer(m))    
    while m != m1:
        m = m1[:]
        m1 = rutschen(m,leer(m))    
    #showMatrix(m)
    return tuple(m)

def links(m):
    tmp = []
    for e in m:
        zahl,x,y,laenge,richt = e
        if richt:
            xn = (N-1)-y
            yn = x
        else:
            xn = (N-1)-y-(laenge-1)
            yn = x
        neu = (zahl,xn,yn,laenge,not richt)
        tmp.append(neu)

    return tuple(tmp)   

def rutschen(m,lm):
    tmp = []
    zaehl = 0
    for e in m:
        zahl,x,y,laenge,richt = e
        pl = platz(m,lm,e)
        zaehl = zaehl + pl
        tmp.append((zahl,x+pl,y,laenge,richt))
    return tmp
    
def rechts(m):
    tmp = []

    for e in m:
        zahl,x,y,laenge,richt = e
        if richt:
            xn = y
            yn = (N-1)-x-(laenge-1)
        else:
            xn = y
            yn = (N-1)-x
        neu = (zahl,xn,yn,laenge,not richt)
        tmp.append(neu)
    
    return tuple(tmp)   


def leer(m):
    tmp = [['.'] * N for i in range(N)]
    
    for e in m:
        zahl,x,y,laenge,richt = e
        for i in range(laenge):
            tmp[x][y]='x'
            if richt:
                x+=1
            else:
                y+=1
    return tmp            
            
def platz(m,lm,e):

    '''
    m: Belegungsmatrix
    lm: Leermatrix
    e: Element aus m
    returns: wieviel Platz unterhalb von e zu rutschen ist.
    '''
    zahl,x,y,laenge,richt = e
    if zahl == 'x': return 0
    zaehl = 0
    
    if richt:
        x = x + laenge 
        while lm[x][y] == '.' and x < N-1:
            x+=1
            zaehl+=1
        return zaehl
    else:
       
        fertig = False
        x = x + 1
        while not fertig and x < N-1:
            for i in range(laenge):
                if lm[x][y+i] != '.':
                    fertig = True
                    break
            if not fertig:
                zaehl+=1
                x+=1
        return zaehl
                
def startstate3():
    global N
    N = 10
    state = ( \
    (0,7,3,2,True), \
    (1,5,4,2,False),\
    (2,6,4,2,True), \
    (3,7,5,2,False), \
    (4,8,1,2,False), \
    (5,4,8,2,True), \
    (6,8,4,5,False), \
    (7,4,5,3,False),  \
    (8,6,6,3,False),  \
    (9,7,1,2,False),  \
    ('x',9,5,1,True))   
    return state
'''
10
##########
#        #
#        #
#        #
#    7775#
#   11  5#
#   2 888#
#990233  #
#44066666#
##### ####
'''        
        
        
def startstate():
    state = ( \
    (0,1,6,2,True), \
    (1,3,1,2,False),\
    (2,3,3,4,False), \
    (3,4,1,2,False), \
    (5,5,1,2,False), \
    (6,6,1,3,False), \
    (4,4,6,3,True),  \
    ('x',7,3,1,True))   
    return state

def nextstates(m):
    return [linksR(m), rechtsR(m)]

def goaltest(m):
    for e in m:
        if e[0] == 'x':
            xg,yg = e[1],e[2]
    if xg != N-1: return False
    for e in m:
        zahl,x,y,laenge,richt = e
        if richt:
            if y == yg and x + laenge +1 == N:
                return True
    return False    
        
def test1():    
    
    m = startstate()
    print(goaltest(m))
    showMatrix(m)
    m = linksR(m)
    m = linksR(m)
    m = linksR(m)
    m = linksR(m)
    m = rechtsR(m)
    m = linksR(m)
    print(goaltest(m))


import time
from collections import deque
start = time.perf_counter()

s = startstate3()          # wahl der eingabe

explored = set()  
nrExplored = 0
prev = {s:None}
frontier = deque([s])       # Queue append und popleft() for bfs
#frontier = [s]
frontierSet = {s}
while frontier:
    state = frontier.popleft()  
    #state = frontier.pop()
    explored.add(state)
    nrExplored += 1
    
    if goaltest(state):
        break
   
    nb = nextstates(state)
    for v in nb:
        # wenn man hier frontier statt frontierSet nimmt,
        # erhöht sich die Laufzeit erheblich
        if v not in explored and v not in frontierSet:
            frontier.append(v)
            frontierSet.add(v)
            prev[v] = state

laufzeit = time.perf_counter()-start
print('#explored: ',nrExplored ,laufzeit)     



# -*- coding: utf-8 -*-
'''
Das Spiel besteht aus 7 Spalten, die jeweils mit bis zu 6 Steinen 
gefüllt werden können.
Eine Stellung wird repräsentiert durch eine Liste von Zahlen
von 0 bis 6, die jeweils angeben, in welcher Reihenfolge Steine
in welche Spalte geworfen wurden.

Die Liste [2,3,2,4] repräsentiert also die folgende Stellung:
    
    x
    x o o
. . . . . . .
0 1 2 3 4 5 6

'''

inf = float('inf')
def maximize(state,alpha,beta,bremse):
    '''
    state: Stellung
    returns: (st, k), die Folgestellung st, die die höchste
    Utlity k hat
    '''

    if bremse >= BREMSE or terminal_test(state):
        return None,evaluation(state)
    
    v, bestChild = -inf, None
    for child in nextstates(state):
        _,utility = minimize(child,alpha,beta,bremse+1)
        if utility > v:
            bestChild, v = child, utility
        if v >= beta:
            break
        if v > alpha:
            alpha = v
    return bestChild, v

def minimize(state,alpha,beta,bremse):
    '''
    state: Stellung
    returns: (st, k), die Folgestellung st, die die niedrigste
    Utlity k hat
    ''' 

    if bremse >= BREMSE or terminal_test(state):
        return None,evaluation(state)

    v, minChild = inf, None
    for child in nextstates(state):
        _,utility = maximize(child,alpha,beta,bremse+1)
        if utility < v:
            minChild, v = child, utility
        if v <= alpha:
            break
        if v < beta:
            beta = v
    return minChild, v  

def nextstates(state):
    '''
    state: Spielstatus
    returns: Liste mit möglichen Folgestellungen
    '''
    anz = [0] * 7   # Liste für die Anzahlen von 0 ... 6 in state
    for k in state:
        anz[k]+=1
    tmp = []
    for i in range(7):
        if anz[i] < 6:
            state_neu = state[:]
            state_neu.append(i)
            tmp.append(state_neu)
    return tmp

def evaluation(state):
    '''
    state: Spielstellung
    returns int - Bewertung der Spielstellung
    '''
    
    w = 0
    for s in muster(state):
        if 'xxxx' in s: return 100000
        if 'oooo' in s: return -100000
        
        if '.xx' in s: w+=5
        if 'xx.' in s: w+=5
        if '.xxx' in s: w+=5
        if 'xxx.' in s: w+=5
        if 'xx.x' in s: w+=5
        if 'x.xx' in s: w+=5
        
        if '.oo' in s: w+=-5
        if 'oo.' in s: w+=-5
        if '.ooo' in s: w+=-5
        if 'ooo.' in s: w+=-5
        if 'oo.o' in s: w+=-5
        if 'o.oo' in s: w+=-5
        
    return w  

def terminal_test(state):
    w = evaluation(state)
    return  w == 100000 or w == -100000 or len(state) == 42

#------------------- Hilfsfunktionen

def muster(state):
    ''' Hilfsfunktion für die Bewertung der Stellung
    state: eine Spielstellung
    returns eine Liste von Strings, die jeweils Reihen
        der Zeilen, Spalten, Diagonalen sind, mindestens mit Länge 4
    ''' 
    temp = []
    m = spalten(state)
    # die zeilen
    for z in m:
        temp.append(z)
   
    # die Spalten
    for j in range(6):
        a = [m[i][j] for i in range(7)]
        temp.append(''.join(a))

    temp.append(getDiagonale(m,0,2,1,4))
    temp.append(getDiagonale(m,0,1,1,5))
    temp.append(getDiagonale(m,0,0,1,6))
    temp.append(getDiagonale(m,1,0,1,6))
    temp.append(getDiagonale(m,2,0,1,5))
    temp.append(getDiagonale(m,3,0,1,4))
    
    temp.append(getDiagonale(m,3,0,-1,4))
    temp.append(getDiagonale(m,4,0,-1,5))
    temp.append(getDiagonale(m,5,0,-1,6))
    temp.append(getDiagonale(m,6,0,-1,6))
    temp.append(getDiagonale(m,6,1,-1,5))
    temp.append(getDiagonale(m,6,2,-1,4))
 
    return temp

def spalten(state):
    ''' Hilfsfunktion für die Funktion muster
    state: Spielstellung
    returns: Liste mit Strings, die die Spalten abbilden
    '''
    tmp = ['' for i in range(7)]
    
    for i in range(len(state)):
        if i % 2 == 0:
            zeichen = 'x'
        else:
            zeichen = 'o'
        tmp[state[i]]+=zeichen
    
    tmp1 = []
    for s in tmp:
        tmp1.append(s.ljust(7,'.'))
    return tmp1

def getDiagonale(m,x,y,increment,laenge):
    ''' Hilfsfunktion für die Funktion muster
    m: Liste mit den Spalten
    x, y, increment, laenge: int
    returns: String, den man erhält, wenn man in der state-Matrix 
       von Position (x,y) in Diagonalrichtung increment
       (+1 = nach rechts unten, -1 nach rechts oben) in der
       Länge laenge geht.
    '''
    s = m[x][y]
    for i in range(laenge-1):
        x+=increment
        y+=1
        s+= m[x][y]
    return s
# -------------------------Ausgabe 

def showstate(state):
    '''
    returns: nichts, druckt die Stellung aus
    '''
    m = spalten(state)
    for j in range(5,-1,-1):
        for i in range(7):
            print(m[i][j], end=' ')
        print()
    print('======='*2)
    print('0 1 2 3 4 5 6')
     

BREMSE = 8
m = []
print('Spieler beginnt mit x ...  ')
while not terminal_test(m):
    showstate(m)
    eingabe = int(input("Bitte 1 Zahl eingeben (Spalte von 0-6): "))
    m.append(eingabe)
    if not terminal_test(m):
        m, _ = minimize(m,-inf,inf,1)

showstate(m)
if evaluation(m) == 100000: print("Spieler x hat gewonnen")
elif evaluation(m) == -100000: print("Spieler o (= Computer) hat gewonnen")
else: print("Unentschieden")  
            

    

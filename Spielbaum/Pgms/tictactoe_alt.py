# -*- coding: utf-8 -*-
'''
Eine Spielstellung ist eine Liste von Zahlen. Jede Zahl ist die
Nummer eines Feldes.

 x . .       0  1  2
 . o .       3  4  5
 . . .       6  7  8

ist repräsentiert durch die Liste [0,4]. Der Maximizer (x) beginnt das Spiel

'''

inf = float('inf')
def maximize(state):
    if terminal_test(state):
        return None,evaluation(state)
    
    v, bestChild = -inf, None
    for child in nextstates(state):
        _,utility = minimize(child)
        if utility > v:
            bestChild,v = child,utility
    return bestChild,v

def minimize(state):
    if terminal_test(state):
        return None,evaluation(state)

    v, bestChild = inf, None
    for child in nextstates(state):
        _,utility = maximize(child)
        if utility < v:
            bestChild,v = child,utility
    return bestChild,v

def nextstates(state):
    '''
    state: Spielstellung
    returns: Liste mit möglichen Folgestellungen (also Liste von Listen)
    '''
    stateset = set(state)
    temp = []
    for i in range(9):
        if i not in stateset:
            nxt = state[:]
            nxt.append(i)
            temp.append(nxt)
    return temp   
       
def terminal_test(state):
    '''
    state: Stellung
    returns: True, wenn Stellung ein Blatt ist
    '''
    w = evaluation(state)
    return w == 1 or w == -1 or len(state) >= 9

def evaluation(state):
    '''
    state: Stellung
    returns: Zahl, die den Wert der Stellung wiedergibt
    '''
    gewinnSets = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
    maxzuege = set(state[::2])
    minzuege = set(state[1::2])
    for g in gewinnSets:
        if g.issubset(maxzuege): return 1
        if g.issubset(minzuege): return -1
    return 0                     

def show(state):
    '''
    state: Spielstellung
    returns: None, printed die Stellung
    '''
    m= [list('...'),list('...'),list('...')]

    for i in range(len(state)):
        if i % 2 == 0:
            c = 'x'
        else:
            c = 'o'
        zeile = state[i] // 3
        spalte = state[i] % 3 
        m[zeile][spalte] = c
    
    for z in range(0,3):
        for s in range(0,3):
            print(m[z][s],end=' ')
        print()

def showMuster():
    '''
    Hilfsfunktion, die die Nummerierung der Felder zeigt
    '''
    for z in range(0,9):
        if z % 3 == 0:
            print()
        print(z,end=' ')
    print()

   
def play():
    state = []
    i = 0
    while not terminal_test(state):
        showMuster()
        if i % 2==0:
            z = int(input("Eingabe Spieler x: "))
            state.append(z)
        else:
            state, _ = minimize(state)
        show(state)
        i += 1
        
    if evaluation(state) == 1:
        print("Spieler x hat gewonnen")
    elif evaluation(state) == -1:
        print("Computer hat gewonnen")
    else:
        print("Unentschieden")
    

    



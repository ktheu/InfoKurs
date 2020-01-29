# -*- coding: utf-8 -*-
'''
Das Spiel besteht aus 7 Spalten, die jeweils mit bis zu 6 Steinen 
gefüllt werden können.
Eine Stellung wird repräsentiert durch eine Liste von Zahlen
von 0 bis 41, die jeweils angeben, in welcher Reihenfolge Steine
auf die jeweilige Position gekommen sind. 
    
 0  1  2  3  4  5  6 
 7  8  9 10 11 12 13 
14 15 16 17 18 19 20 
21 22 23 24 25 26 27 
28 29 30 31 32 33 34 
35 36 37 38 39 40 41 

Der erste Stein ist 'x'.
Die Liste [38,37,30] repräsentiert also die folgende Stellung:

. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . x . . . . 
. . o x . . . 
=============
0 1 2 3 4 5 6

Im User-Interface gibt man die Nummer der Spalte für den nächsten Stein an.

'''
inf = float('inf')

def maximize(state, alpha=-inf, beta=inf, bremse=4):

    if bremse == 0 or terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, -inf

    for st in nextstates(state):
        _, k = minimize(st, alpha, beta, bremse-1)
        if k > best_k:
            best_st, best_k = st, k
        if best_k >= beta:
            break
        if best_k > alpha:
            alpha = best_k
    return best_st, best_k


def minimize(state, alpha=-inf, beta=inf, bremse=4):

    if bremse == 0 or terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, inf
    for st in nextstates(state)[::-1]:
       
        _, k = maximize(st, alpha, beta, bremse-1)
        if bremse == 8: print(st, k)
        if k < best_k:
            best_st, best_k = st, k
        if best_k <= alpha:
            break
        if best_k < beta:
            beta = best_k
    return best_st, best_k

def showNr():
    ''' printed die Nummerierung der Felder '''
    for i in range(42):
        if i % 7 == 0:
            print()
        print('{:2d}'.format(i), end=' ')
    print()

def getBoard(state):  
    ''' wandelt state in ein board um '''
    tmp = list('.'*42)
    for i in range(len(state)):
        if i % 2 == 0:
            tmp[state[i]] = 'x'
        else:
            tmp[state[i]] = 'o'
    return tmp

def showBoard(board):
    ''' printed board '''
    for i in range(42):
        if i % 7 == 0:
            print()
        print('{:1s}'.format(board[i]), end=' ')
    print()
    print('='*13)
    print('0 1 2 3 4 5 6')

def muster(board):
    tmp = []
    for i in range(0,42,7):
        tmp.append(''.join(board[i:i+7]))  # horizontal
    for i in range(7):
        tmp.append(''.join(board[i::7]))   # vertikal

    # diagonale muster nach links unten
    tmp.append(''.join(board[14:39:8]))
    tmp.append(''.join(board[7:40:8]))
    tmp.append(''.join(board[0:41:8]))
    tmp.append(''.join(board[1:42:8]))
    tmp.append(''.join(board[2:35:8]))
    tmp.append(''.join(board[3:28:8]))
   
    # diagonale muster nach rechts unten 
    tmp.append(''.join(board[3:22:6]))
    tmp.append(''.join(board[4:29:6]))
    tmp.append(''.join(board[5:36:6]))
    tmp.append(''.join(board[6:37:6]))
    tmp.append(''.join(board[13:38:6]))
    tmp.append(''.join(board[20:39:6]))
    return tmp
    
def muster2(board):
    ''' Liste aller Stringmuster (horizontal, vertikal, diagonal) mit Mindestlänge 4 '''
    tmp = []
    for i in range(0,42,7):   # horizontal
        tmp.append(''.join(board[i:i+7]))
     
    for i in range(7):        # vertikal
        tmp.append(''.join(board[i::7]))
    
    # diagonal nach links
    border = [i for i in range(42) if i < 7 or i % 7 == 6]
    for i in border:
       if lenL(i) >= 4:
            tmp.append(diaL(board,i)) 

    # diagonal nach rechts   
    border = [i for i in range(42) if i < 7 or i % 7 == 0]  
    for i in border:
       if lenR(i) >= 4:
            tmp.append(diaR(board,i))  
    
    return tmp

# --- Hilfsfunktionen für muster ------
def lenL(nr):
    ''' Länge des Strings diagonal nach links unten, ausgehend von nr '''
    col, row  = nr % 7, nr // 7
    return min(6-row-1,col) + 1

def lenR(nr):
    ''' Länge des Strings diagonal nach rechts unten, ausgehend von nr '''
    col, row  = nr % 7, nr // 7
    return min(6-row,7-col) 

def diaL(board,nr):
    ''' String diagonal nach links unten, ausgehend von nr '''
    k = lenL(nr)
    end = nr + 6*(k-1)+1
    return ''.join(board[nr:end:6])

def diaR(board,nr):
    ''' String diagonal nach rechts unten, ausgehend von nr '''
    k = lenR(nr)
    end = nr + 8*(k-1)+1
    return ''.join(board[nr:end:8])

# --- Ende der Hilfsfunktionen für muster -----


def nextstates(state):
    '''
    state: Spielstatus
    returns: Liste mit möglichen Folgestellungen
    '''
    board = getBoard(state)
    tmp = []
    for i in free(board):     # für jeden verfügbaren Platz
        tmp.append(state+[i])
    return tmp


def evaluation(state):
    '''
    state: Spielstellung
    returns int - Bewertung der Spielstellung
    '''
    w = 0
    board = getBoard(state)
    for s in muster(board):
        if 'xxxx' in s:
            return inf
        if 'oooo' in s:
            return -inf
        if '.xx' in s:
            w += 5
        if 'xx.' in s:
            w += 5
        if '.xxx' in s:
            w += 5
        if 'xxx.' in s:
            w += 5
        if 'xx.x' in s:
            w += 5
        if 'x.xx' in s:
            w += 5
        if '.oo' in s:
            w += -5
        if 'oo.' in s:
            w += -5
        if '.ooo' in s:
            w += -5
        if 'ooo.' in s:
            w += -5
        if 'oo.o' in s:
            w += -5
        if 'o.oo' in s:
            w += -5
    return w

def terminal_test(state):
    w = evaluation(state)
    return w == inf or w == -inf or len(state) == 42

def colNrs(i):
    '''
    i: int,  0 <= i <= 6
    returns: Liste der Platznummern für Spalte i, von unten nach oben
    '''
    return [35+i-7*r for r in range(0,6)]

def freeIn(board,i):
    ''' returns: nächster freier Platz in Spalte i '''
    for j in colNrs(i):
        if board[j] == '.':
            return j

def free(board):
    ''' liste der möglichen nächsten positionen '''
    tmp = []
    for i in range(7):
       for j in colNrs(i):
           if board[j] == '.':
               tmp.append(j)
               break
    return tmp

def play():
    ''' Mensch spielt zuerst '''

    i = 0
    k = None         # Bewertung
    x = None         # letzter Zug

    state = []
    board = getBoard(state)
    showBoard(board)

    while not terminal_test(state):
         
        if i % 2==0:
            x = int(input("Eingabe Spieler (0-6): "))
            state.append(freeIn(board,x))

        else:
            if tuple(state) in buch:
                state = buch[tuple(state)]
            else:
                state, k = minimize(state,bremse=8)
       
        
        board = getBoard(state)
        showBoard(board)
        print("Zug: ",x,"Bewertung: ", k)
        i = i+1

    showBoard(board)
    if evaluation(state) == inf:
        print("Spieler x hat gewonnen")
    elif evaluation(state) == -inf:
        print("Computer hat gewonnen")
    else:
        print("Unentschieden")

def playC():
    ''' Computer spielt zuerst '''
    state = []
    i = 0
    k = None
    x = None
    while not terminal_test(state):
        board = getBoard(state)
        #showNr()
         
        if i % 2==1:
            x = int(input("Eingabe Spieler o: "))
            state.append(freeIn(board,x))

        else:
            if tuple(state) in buch:
                state = buch[tuple(state)]
            else:
                state, k = maximize(state,bremse=8)
           
        board = getBoard(state)
        showBoard(board)
        print("Zug: ",x,"Bewertung: ", k)
        i = i+1

    showBoard(board)
    if evaluation(state) == inf:
        print("Spieler o hat gewonnen")
    elif evaluation(state) == inf:
        print("Computer hat gewonnen")
    else:
        print("Unentschieden")


buch = {tuple():[38],(38,):[38,37]}   # Eröffnungsbuch

showNr()

#state = [38,37,31,24,30,17,23,10,3,16,39,32,40]

state = [38,37,30]


board = getBoard(state)
showBoard(board)
#print(minimize(state,bremse=8))


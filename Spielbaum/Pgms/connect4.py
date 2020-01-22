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


def maximize(state, alpha, beta, bremse):
    '''
    state: Stellung
    returns: (st, k), die Folgestellung st, die die höchste
    Utlity k hat
    '''

    if bremse >= BREMSE or terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, -inf

    for st in nextstates(state):
        _, k = minimize(st, alpha, beta, bremse+1)
        if k > best_k:
            best_st, best_k = st, k
        if best_k >= beta:
            break
        if best_k > alpha:
            alpha = best_k
    return best_st, best_k


def minimize(state, alpha, beta, bremse):
    '''
    state: Stellung
    returns: (st, k), die Folgestellung st, die die niedrigste
    Utlity k hat
    '''

    if bremse >= BREMSE or terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, inf
    for st in nextstates(state):
        _, k = maximize(st, alpha, beta, bremse+1)
        if k < best_k:
            best_st, best_k = st, k
        if best_k <= alpha:
            break
        if best_k < beta:
            beta = best_k
    return best_st, best_k


def nextstates(state):
    '''
    state: Spielstatus
    returns: Liste mit möglichen Folgestellungen
    '''
    tmp = []
    for i in range(7):
        if state.count(i) < 6:
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
            return 100000
        if 'oooo' in s:
            return -100000

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
    return w == 100000 or w == -100000 or len(state) == 42

#------------------- Hilfsfunktionen

def muster(board):
    tmp = []
    for i in range(0,36,7):
        tmp.append(''.join(board[i:i+7]))
    for i in range(0,7):
        tmp.append(''.join(board[i:i+36:7]))
    # diagonale muster
    tmp.append(''.join(board[14::8]))
    tmp.append(''.join(board[7::8]))
    tmp.append(''.join(board[0::8]))
    tmp.append(''.join(board[1::8]))
    tmp.append(''.join(board[2:35:8]))
    tmp.append(''.join(board[3:28:8]))
    tmp.append(''.join(board[3:22:6]))
    tmp.append(''.join(board[4:29:6]))
    tmp.append(''.join(board[5:36:6]))
    tmp.append(''.join(board[6:37:6]))
    tmp.append(''.join(board[13:38:6]))
    tmp.append(''.join(board[20:39:6]))
    return tmp

def p(i):
    '''
    i: int, columnNr,  0 <= i <= 6
    returns: list of boardnr for column i
    
    e.g: p(3) is the list of positions for column 3
    '''
    return [35+i-7*r for r in range(0,6)]

def getBoard(state):
    board = list('.'*42)
    zug = 0
    for x in state:
        posList = p(x)
        i = 0
        while board[posList[i]] != '.': i+=1
        if zug % 2 == 0:
            board[posList[i]] = 'x'
        else:
            board[posList[i]] = 'o'
        zug +=1
    return board

def showBoard(board):
    board = getBoard(state)
    for i in range(6):
        print(' '.join(board[i*7:(i+1)*7]))
    print('='*13)
    print('0 1 2 3 4 5 6')
        
BREMSE = 8
state = []
print('Spieler beginnt mit x ...  ')
while not terminal_test(state):
    board = getBoard(state)
    showBoard(board)
    eingabe = int(input("Bitte 1 Zahl eingeben (Spalte von 0-6): "))
    state.append(eingabe)
    if not terminal_test(state):
        state, _ = minimize(state, -inf, inf, 1)

 
board = getBoard(state)
showBoard(board)
if evaluation(state) == 100000:
    print("Spieler x hat gewonnen")
elif evaluation(state) == -100000:
    print("Spieler o (= Computer) hat gewonnen")
else:
    print("Unentschieden")


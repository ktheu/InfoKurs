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
gewinn = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6},
          {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]


def maximize(state):
    if terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, -inf
    for st in nextstates(state):
        _, k = minimize(st)
        if k > best_k:
            best_st, best_k = st, k
    return best_st, best_k


def minimize(state):
    if terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, inf
    for st in nextstates(state):
        _, k = maximize(st)
        if k < best_k:
            best_st, best_k = st, k
    return best_st, best_k


def nextstates(state):
    '''
    state: Spielstellung
    returns: Liste mit möglichen Folgestellungen (also Liste von Listen)
    '''
    temp = []
    for i in range(9):
        if i not in state:
            temp.append(state+[i])
    return temp


def terminal_test(state):
    '''
    state: Stellung
    returns: True, wenn Stellung ein Blatt ist
    '''
    w = evaluation(state)
    return w == 1 or w == -1 or len(state) == 9


def evaluation(state):
    '''
    state: Stellung
    returns: Zahl, die den Wert der Stellung wiedergibt
    '''

    maxzuege = set(state[::2])
    minzuege = set(state[1::2])
    for g in gewinn:
        if g.issubset(maxzuege):
            return 1
        if g.issubset(minzuege):
            return -1
    return 0


def show(state):
    '''
    state: Spielstellung
    returns: None, printed die Stellung
    '''
    a = ['.'] * 9
    for i in range(len(state)):
        if (i % 2 == 0):
            a[state[i]] = 'x'
        else:
            a[state[i]] = 'o'

    for i in range(9):
        if i % 3 == 0:
            print()
        print(a[i], end=' ')
    print()


def showMuster():
    '''
    Hilfsfunktion, die die Nummerierung der Felder zeigt
    '''
    for i in range(0, 9):
        if i % 3 == 0:
            print()
        print(i, end=' ')
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

play()
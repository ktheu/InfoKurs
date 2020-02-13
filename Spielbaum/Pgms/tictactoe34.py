'''
Eine Spielstellung ist eine Liste von Zahlen. Jede Zahl ist die
Nummer eines Feldes.

 x . . .     0  1  2  3
 . o . .     4  5  6  7
 . . . .     8  9 10 11

ist repräsentiert durch die Liste [0,5]. Der Maximizer (x) beginnt das Spiel

'''

# Mit Buch
# Mit tiefe: Je schneller der Gewinn, desto höher die Punktezahl

inf = float('inf')
gewinn = [{0, 1, 2}, {1, 2, 3}, {4, 5, 6}, {5, 6, 7},
          {8, 9, 10}, {9, 10, 11}, {0, 4, 8}, {1, 5, 9}, {2, 6, 10},
          {3, 7, 11}, {0, 5, 10},{1,6,11},{2,5,8},{3,6,9}]


def maximize(state, tiefe):
    if terminal_test(state, tiefe):
        return None, evaluation(state, tiefe)

    best_st, best_k = None, -inf
    for st in nextstates(state):
        _, k = minimize(st, tiefe+1)
        if k > best_k:
            best_st, best_k = st, k
    return best_st, best_k


def minimize(state, tiefe):
    if terminal_test(state, tiefe):
        return None, evaluation(state, tiefe)

    best_st, best_k = None, inf
    for st in nextstates(state):
        _, k = maximize(st, tiefe)
        if k < best_k:
            best_st, best_k = st, k
    return best_st, best_k


def nextstates(state):
    '''
    state: Spielstellung
    returns: Liste mit möglichen Folgestellungen (also Liste von Listen)
    '''
    temp = []
    for i in range(12):
        if i not in state:
            temp.append(state+[i])
    return temp


def terminal_test(state, tiefe):
    '''
    state: Stellung
    returns: True, wenn Stellung ein Blatt ist
    '''
    w = evaluation(state, tiefe)
    return w > 1 or w < -1 or len(state) == 12


def evaluation(state, tiefe):
    '''
    state: Stellung
    returns: Zahl, die den Wert der Stellung wiedergibt
    '''

    maxzuege = set(state[::2])
    minzuege = set(state[1::2])

    for g in gewinn:
        if g <= maxzuege:
            return 100 - tiefe
        if g <= minzuege:
            return -100 + tiefe
    return 0


def show(state):
    '''
    state: Spielstellung
    returns: None, printed die Stellung
    '''
    a = ['.'] * 12
    for i in range(len(state)):
        if (i % 2 == 0):
            a[state[i]] = 'x'
        else:
            a[state[i]] = 'o'

    for i in range(12):
        if i % 4 == 0:
            print()
        print(a[i], end=' ')
    print()


def showMuster():
    '''
    Hilfsfunktion, die die Nummerierung der Felder zeigt
    '''
    for i in range(0, 12):
        if i % 4 == 0:
            print()
        print(i, end=' ')
    print()


def play():
    state = []
    tiefe = 0
    i = 0
    while not terminal_test(state, tiefe):

        if i % 2==0:
            showMuster()
            z = int(input("Eingabe Spieler x: "))
            state.append(z)
        else:
            if tuple(state) in buch:
                state = buch[tuple(state)]
            else:
               state, _ = minimize(state, tiefe+1)
        show(state)
        i += 1

    if evaluation(state, tiefe) > 1:
        print("Spieler x hat gewonnen")
    elif evaluation(state, tiefe) < -1:
        print("Computer hat gewonnen")
    else:
        print("Unentschieden")

def playC():
    state = []
    tiefe = 0
    i = 0
    while not terminal_test(state, tiefe):

        if i % 2==1:
            showMuster()
            z = int(input("Eingabe Spieler o: "))
            state.append(z)
        else:
            if tuple(state) in buch:
                state = buch[tuple(state)]
            else:
               state, _ = maximize(state, tiefe+1)
        show(state)
        i += 1

    if evaluation(state, tiefe) > 1:
        print("Computer x hat gewonnen")
    elif evaluation(state, tiefe) < -1:
        print("Spieler o gewonnen")
    else:
        print("Unentschieden")

buch = {(5,):[5,6], tuple() : [5]}

playC()
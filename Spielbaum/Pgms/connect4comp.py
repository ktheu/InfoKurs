inf = float('inf')

def maximize(state, alpha=-inf, beta=inf, bremse=6, evaluation=None):

    if bremse == 0 or terminal_test(state, evaluation):
        return None, evaluation(state)

    best_st, best_k = None, -inf

    for st in nextstates(state):
        _, k = minimize(st, alpha, beta, bremse-1, evaluation)
        if best_st is None:
            best_st = st
        if k > best_k:
            best_st, best_k = st, k
        if best_k >= beta:
            break
        if best_k > alpha:
            alpha = best_k
    return best_st, best_k


def minimize(state, alpha=-inf, beta=inf, bremse=6, evaluation=None):

    if bremse == 0 or terminal_test(state, evaluation):
        return None, evaluation(state)

    best_st, best_k = None, inf
    for st in nextstates(state):
        _, k = maximize(st, alpha, beta, bremse-1, evaluation)
        if best_st is None:
            best_st = st
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
    ''' wandelt state in ein board um 
        ein board ist eine Liste mit 42 Zeichen, entweder x, o oder ein Punkt.'''
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
    for i in range(0, 42, 7):
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


def terminal_test(state, evaluation):
    w = evaluation(state)
    return w == inf or w == -inf or len(state) == 42


def colNrs(i):
    '''
    i: int,  0 <= i <= 6
    returns: Liste der Platznummern für Spalte i, von unten nach oben
    '''
    return [35+i-7*r for r in range(0, 6)]


def freeIn(board, i):
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


def evalA(state):
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


def evalB(state):
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
        if 'x...' in s:
            w += 5
        if '.x..' in s:
            w += 5
        if '..x.' in s:
            w += 5
        if '...x' in s:
            w += 5

        if 'xx..' in s:
            w += 30
        if 'x.x.' in s:
            w += 30
        if 'x..x' in s:
            w += 30
        if '.xx.' in s:
            w += 30
        if '.x.x' in s:
            w += 30
        if '..xx' in s:
            w += 30
        if 'xxx.' in s:
            w += 500
        if 'xx.x' in s:
            w += 500
        if 'x.xx' in s:
            w += 500
        if '.xxx' in s:
            w += 500

        if 'o...' in s:
            w += -5
        if '.o..' in s:
            w += -5
        if '..o.' in s:
            w += -5
        if '...o' in s:
            w += -5

        if 'oo..' in s:
            w += -30
        if 'o.o.' in s:
            w += -30
        if 'o..o' in s:
            w += -30
        if '.oo.' in s:
            w += -30
        if '.o.o' in s:
            w += -30
        if '..oo' in s:
            w += -30
        if 'ooo.' in s:
            w += -500
        if 'oo.o' in s:
            w += -500
        if 'o.oo' in s:
            w += -500
        if '.ooo' in s:
            w += -500
    return w


def playAB():
    ''' evalA startet mit x
    evalB ist Nachziehender mit o.
    '''

    BREMSE = 8
    state = []
    board = getBoard(state)
    showBoard(board)

    i = 0
    while not terminal_test(state, evaluation=evalA):

        if i % 2 == 0:
            state, k = maximize(state, bremse=BREMSE, evaluation=evalA)
            board = getBoard(state)
            showBoard(board)
            print(state)
            print("evalA x hat gezogen",
                  state[-1] % 7, " - evalA/evalB-Bewertung:", evalA(state), evalB(state), "- max-Wert:", k)

        else:
            state, k = minimize(state, bremse=BREMSE, evaluation=evalB)
            board = getBoard(state)
            showBoard(board)
            print(state)
            print("evalB o hat gezogen",
                  state[-1] % 7, " - evalA/evalB-Bewertung:", evalA(state), evalB(state), "- min-Wert:", k)

        i = i+1

    if evalA(state) == inf:
        print("evalA x hat gewonnen")
    elif evalA(state) == -inf:
        print("evalB o  hat gewonnen")
    else:
        print("Unentschieden")

playAB()


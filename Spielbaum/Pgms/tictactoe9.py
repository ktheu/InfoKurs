from muster import *
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

    if bremse ==0 or terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, inf
    for st in nextstates(state):
        _, k = maximize(st, alpha, beta, bremse-1)
        if k < best_k:
            best_st, best_k = st, k
        if best_k <= alpha:
            break
        if best_k < beta:
            beta = best_k
    return best_st, best_k

def nextstates(state):
    temp = []
    for i in range(n):
        if i not in state:
            temp.append(state+[i])
    return temp


def terminal_test(state):
    w = evaluation(state)
    return w == 10000 or w == -10000 or len(state) == n


def evaluation(state):
    board = getBoard(n, rows, state)
    w = 0
    for s in muster(board, rows, 4):
        if 'xxxx' in s:
                return 10000
        if 'oooo' in s:
            return -10000

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
        if '.xxx.' in s:
            w += 5000
  
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
        if '.ooo.' in s:
            w += 5000
    return w

def play():
    state = []
    i = 0
    k = 0
    while not terminal_test(state):

        board = getBoard(n,rows,state)
        showNr(n,rows)
        showBoard(board,rows)
        
        if i % 2==0:
            z = int(input("Eingabe Spieler x: "))
            state.append(z)

        else:
            state, k = minimize(state)
            
           
        board = getBoard(n,rows,state)
        # showBoard(board,rows)
        print("Bewertung: ", k)
        i += 1
        
    if evaluation(state) == 10000:
        print("Spieler x hat gewonnen")
    elif evaluation(state) == -10000:
        print("Computer hat gewonnen")
    else:
        print("Unentschieden")


rows, cols = 5,5
n = rows*cols
play()
# state = [0,5,1,6,2,7,3]
# board = getBoard(n,rows,state)
# showBoard(board,rows)
# print(muster(board,rows,4))
# print(evaluation(state))
# print('thinking about')
# print(minimize([12,7,6]))
# state = [12,7,6]
# board = getBoard(n,rows,state)
# showBoard(board,rows)
# showNr(n,rows)
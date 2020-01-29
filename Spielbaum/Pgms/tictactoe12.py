inf = float('inf')
horizontal = [{0,1,2},{1,2,3},{4,5,6},{5,6,7},{8,9,10},{9,10,11}]
vertikal = [{0,4,8},{1,5,9},{2,6,10},{3,7,11}]
diagonal = [{0,5,10},{1,6,11},{8,5,2},{9,6,3}]
gewinn = horizontal + vertikal + diagonal

def terminal_test(state):
    return evaluation(state) > 1 or evaluation(state) < -1 or len(state) >= 12

def evaluation(state):
    maxzuege = set(state[::2])
    minzuege = set(state[1::2])
    for g in gewinn:
        if g.issubset(maxzuege): return 1000 - len(state)
        if g.issubset(minzuege): return -1000 + len(state)

    return 0    

def nextstates(state):
    temp = []
    for i in range(12):
        if i not in state:
            temp.append(state + [i])
    return temp

def maximize(state):
    # returns: (st, k) - die Folgestellung mit höchster Utility, k die utility von st
    if terminal_test(state):
        return None, evaluation(state)
    
    bestChild = None
    bestUtil = -inf
    for nextChild in nextstates(state):
        _, nextUtil = minimize(nextChild)
        if nextUtil > bestUtil:
            bestUtil = nextUtil
            bestChild = nextChild
 
    return bestChild, bestUtil

def minimize(state):
    # returns: (st, k) - die Folgestellung mit niedrigster Utility, k die utility von st
    if terminal_test(state):
        return None, evaluation(state)

    bestChild = None
    bestUtil = inf
  
    for st in nextstates(state):
        nextChild, nextUtil = maximize(st)
        if nextUtil < bestUtil:
            bestUtil = nextUtil
            bestChild = st

    return bestChild, bestUtil


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
        if i % 4 == 0: print()
        print(a[i],end= ' ')
    print()

def showMuster():
    '''
    Hilfsfunktion, die die Nummerierung der Felder zeigt
    '''
    for i in range(0,12):
        if i % 4 == 0: print()
        print('{:2d}'.format(i),end=' ')
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
            if tuple(state) in buch:
                state = buch[tuple(state)]
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

def playC():
    state = []
    i = 0
    while not terminal_test(state):
        showMuster()
        if i % 2==1:
            z = int(input("Eingabe Spieler o: "))
            state.append(z)
        else:
            if tuple(state) in buch:
                state = buch[tuple(state)]
            else:    
                state, _ = maximize(state)
        show(state)
   
        i += 1
        
    if evaluation(state) == -1:
        print("Spieler o hat gewonnen")
    elif evaluation(state) == 1:
        print("Computer hat gewonnen")
    else:
        print("Unentschieden")
        


buch = {(0,):[0,1], (0,1,5):[0,1,5,10], tuple():[0]}          
 
 
 
play()


    

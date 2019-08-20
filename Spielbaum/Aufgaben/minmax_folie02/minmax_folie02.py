inf = float('inf')
def maximize(state):
    if terminal_test(state):
        return None,evaluation(state)

    v, bestChild = -inf, None
    for child in nextstates(state):
        _,utility = minimize(child)
        if utility > v:
            bestChild,v = child,utility
    print(state+':'+str(v),end=' ')
    return bestChild,v

def minimize(state):
    if terminal_test(state):
        return None,evaluation(state)

    v, bestChild = inf, None
    for child in nextstates(state):
        _,utility = maximize(child)
        if utility < v:
            bestChild,v = child,utility
    print(state+':'+str(v),end=' ')
    return bestChild,v

def nextstates(state):
    return nxt[state]

def terminal_test(state):
    return state in blatt

def evaluation(state):
    return blatt[state]

#  Der Spielbaum aus der Folie
nxt = {'a':list('bc'),'b':list('de'),'c':list('fg')}   # wurzel 'a'
blatt = {'d':10,'e':8,'f':4,'g':50}
best=maximize('a')
print()
print('Bester zug:',best[0])

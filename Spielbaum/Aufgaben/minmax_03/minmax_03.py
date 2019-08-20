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
nxt = {'a':list('bc'),'b':list('de'),'c':list('fg'),'d':list('hi'),
    'e':list('jk'),'f':list('lm'),'g':list('no')}
blatt = {'h':20,'i':-5,'j':32,'k':1,'l':7,'m':-6,'n':2,'o':8}
best=maximize('a')
print()
print('Bester zug:',best[0])

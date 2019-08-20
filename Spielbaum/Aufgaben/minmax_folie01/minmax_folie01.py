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
nxt = {'a':list('bcd'),'b':list('ef'),'c':list('ghi'),'d':list('j'),'e':list('kl'),
       'f':list('mno'),'g':'p','h':list('qr'),'i':list('st'),'j':list('uvw')}
blatt = {'k':2,'l':-4,'m':-2,'n':-1,'o':3,'p':4,'q':-2,'r':-5,'s':2,'t':-1,'u':-3,'v':1,'w':-2}
best=maximize('a')
print()
print('Bester zug:',best[0])

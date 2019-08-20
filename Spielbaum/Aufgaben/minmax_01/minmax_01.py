# -*- coding: utf-8 -*-
'''
Was erscheint auf der Konsole?
'''
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

#%%
nxt = {'a':list('bcd'),'b':list('efg'),'c':list('hij'),'d':list('klm')}
blatt = {'e':3,'f':12,'g':8,'h':2,'i':4,'j':6,'k':14,'l':2,'m':5}
best=maximize('a')
print()
print('Bester zug:',best[0])

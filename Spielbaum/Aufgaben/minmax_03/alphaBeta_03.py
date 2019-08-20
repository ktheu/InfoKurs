# -*- coding: utf-8 -*-
inf = float('inf')
def maximize(state,alpha,beta):

    if terminal_test(state):
        print(state,end=' ')
        return None,evaluation(state)

    bestChild, v = None, -inf
    for child in nextstates(state):
        _,utility = minimize(child,alpha,beta)
        if utility > v:
            v, bestChild = utility, child
        if v >= beta:
            print('#',end=' ')
            break
        if v > alpha:
            alpha = v
    return bestChild, v

def minimize(state,alpha,beta):

    if terminal_test(state):
        print(state,end=' ')
        return None,evaluation(state)

    v, bestChild = inf, None
    for child in nextstates(state):
        _,utility = maximize(child,alpha,beta)
        if utility < v:
            v, bestChild = utility, child
        if v <= alpha:
            print('#',end=' ')
            break
        if v < beta:
            beta = v
    return bestChild, v

def decision(state):
    child, _ = maximize(state,-inf,inf)
    return child

def nextstates(state):
    return nxt[state]

def terminal_test(state):
    return state in blatt

def evaluation(state):
    return blatt[state]

nxt = {'a':list('bc'),'b':list('de'),'c':list('fg'),'d':list('hi'),
    'e':list('jk'),'f':list('lm'),'g':list('no')}
blatt = {'h':20,'i':-5,'j':32,'k':1,'l':7,'m':-6,'n':2,'o':8}
best = decision('a')
print('\nBester Zug',best)
#%%
#%% Baum4

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

nxt = {'a':list('bcd'),'b':list('efg'),'c':list('hij'),'d':list('klm')}
blatt = {'e':3,'f':12,'g':8,'h':2,'i':4,'j':6,'k':14,'l':2,'m':5}
best = decision('a')
print('\nBester Zug',best)
#%%
#%% Baum4

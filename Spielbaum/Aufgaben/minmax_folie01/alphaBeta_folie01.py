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

nxt = {'a':list('bcd'),'b':list('ef'),'c':list('ghi'),'d':list('j'),'e':list('kl'),
       'f':list('mno'),'g':'p','h':list('qr'),'i':list('st'),'j':list('uvw')}
blatt = {'k':2,'l':-4,'m':-2,'n':-1,'o':3,'p':4,'q':-2,'r':-5,'s':2,'t':-1,'u':-3,'v':1,'w':-2}
best = decision('a')
print('\nBester Zug',best)
#%%
#%% Baum4

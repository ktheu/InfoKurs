inf = float('inf')

def maximize(state):
    if terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, -inf
    for st in nextstates(state):
        _, k = minimize(st)
        if k > best_k:
            best_st, best_k = st, k
    return best_st, best_k


def minimize(state):
    if terminal_test(state):
        return None, evaluation(state)

    best_st, best_k = None, inf
    for st in nextstates(state):
        _, k = maximize(st)
        if k < best_k:
            best_st, best_k = st, k
    return best_st, best_k


def terminal_test(state):
    return state in blatt

def evaluation(state):
    return blatt[state]

def nextstates(state):
    return nxt[state]

nxt = {'a': list('bc'), 'b':list('de'), 'c':list('fg')}
blatt = {'d': 10, 'e':8, 'f':4, 'g':50}

print(maximize('a'))
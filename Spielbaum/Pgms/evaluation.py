def evaluation(state):
    '''
    state: Spielstellung
    returns int - Bewertung der Spielstellung
    '''
    w = 0
    board = getBoard(state)
    for s in muster(board):
        if 'xxxx' in s:
            return inf
        if 'oooo' in s:
            return -inf
        if 'xx..' in s:
            w += 5
        if '.xx.' in s:
            w += 5
        if '..xx' in s:
            w += 5
        if 'x.x.' in s:
            w += 
        if '.x.x' in s:
            w += 5
        if '.xx.' in s:
            w += 5
        if '.xxx' in s:
            w += 5
        if 'xxx.' in s:
            w += 5
        if 'xx.x' in s:
            w += 5
        if 'x.xx' in s:
            w += 5
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
    return w
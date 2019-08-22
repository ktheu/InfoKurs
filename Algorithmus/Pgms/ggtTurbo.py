def ggtTurbo(a,b):
    '''
    a, b: positive ganze Zahlen
    returns: größten gemeinsamen Teiler von a und b
    '''
    while b != 0:
        a, b = b, a % b
    return a

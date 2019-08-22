def ggtDumm(a,b):
    '''
    a, b: positive ganze Zahlen
    returns: größten gemeinsamen Teiler von a und b
    '''
    teiler = a
    while a % teiler != 0 or b % teiler != 0:
        teiler -= 1
    return teiler

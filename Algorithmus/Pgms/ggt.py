def ggt(a,b):
    '''
    a, b: positive ganze Zahlen
    returns: größten gemeinsamen Teiler von a und b
    '''
    while a != b:
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a

a, b = 44, 80
print('Der ggT von {} und {} ist {}'.format(a,b,ggt(a,b)))

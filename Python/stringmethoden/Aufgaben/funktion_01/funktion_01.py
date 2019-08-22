def func(s, teil):
    '''
    s, teil: Strings
    returns True, wenn s mit teil beginnt oder endet und die Länge
       von s nicht größer ist als die doppelte Länge von Teil

    Beispiele:
    func('abc',ab')

    '''
    return (s.startswith(teil) or s.endswith(teil)) and not len(s) > 2 * len(teil)

s, teil = 'abc', 'ab'
print(func(s,teil))

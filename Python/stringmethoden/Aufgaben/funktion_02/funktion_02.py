def func(s):
    '''
    s: String
    returns True, wenn s mindestens die Länge 5 hat und die ersten beiden
       Zeichen alphanumerisch und die letzten beiden Zeichen Ziffern sind.

    Beispiele:
    >>> func('R2be-09')
    True
    >>> func('A?2b09')
    False
    '''
    return len(s) >= 5 and s[:2].isalnum() and s[-2:].isdigit()


print(func('R2be-09'))
print(func('A?2b09'))

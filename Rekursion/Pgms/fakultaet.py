# rekursiv 
def fakultaet(n):
    '''
    n: ganze Zahl >= 0
    returns: n! (= n Fakultät)
    '''
    if n == 0: return 1
    return n * fakultaet(n-1)

print(fakultaet(4))
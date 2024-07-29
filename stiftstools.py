def collatz(x):
    '''
    x: positive ganze Zahl
    returns: collatz-Zahl von x
    '''
    z = 0
    while x != 1:
        if x % 2 == 0:
            x = x//2
        else:
            x = 3*x + 1
        z += 1
    return z


def ggt(a,b):
    '''
    a, b: positive ganze Zahlen
    returns: größten gemeinsamen Teiler von a und b
    '''
    while b != 0:
        a, b = b, a % b
    return a

def eratosthenes(n):
    '''
    n: positive ganze Zahl
    returns: Liste mit allen Primzahlen <= n
    '''
    tmp = []
    prim = [True] * (n+1)
    for i in range(2,n+1):
        if prim[i]:
            tmp.append(i)
            for j in range(i+i,n+1,i):
                prim[j] = False
    return tmp


def binaereSuche(a, x):
    '''
    a: sortierte Liste mit Zahlen
    x: Zahl
    returns: Index von x in a, falls x in a
             -1              , falls x nicht in a
    '''
    L = 0
    R = len(a)-1
    while L <= R:  
        mid =(L + R) // 2    # mid = L + (R-L)//2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            L = mid + 1
        else:
            R = mid - 1
            
    return -1
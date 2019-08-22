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

print(*eratosthenes(100))

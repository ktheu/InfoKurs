def back(a):
    if isSolution(a):
        solutions.append(a.copy())
        return
    for cand in candidates(a):
        if isGood(cand,a):
            a.append(cand)
            back(a)
            a.pop()
                
def isSolution(a):
    '''
    returns: True, wenn die Teillösung a eine Lösung darstellt
    '''
    return len(a) == n and len(set(a)) == m

def candidates(a):  
    '''
    returns: Liste von Entscheidungen, die die Teillösung a um eine Stufe erweitern können
    '''
    return list(range(1,m+1))

def isGood(cand, a):
    '''
    returns: True, wenn die Entscheidung cand die Teillösung a sinnvoll erweitert.
    '''
    if len(a) == n: return False
    k = len(set(a) | {cand} )      # Anzahl schon vergebener verschiedenen Themen inclusive des aktuellen Kandidaten
    if m-k > n-k: return False     # Anzahl noch zu vergebender Themen ist größer als die Anzahl der noch nicht vergebenen Schüler
    return True

           
n = 5
m = 3
solutions = []
back([])
print(f'Es gibt {len(solutions)} Möglichkeiten:')
for x in solutions:
    print(*x)
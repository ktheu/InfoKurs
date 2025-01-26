def back(a):
    if isSolution(a):
        solutions.append(a.copy())
        return
    for cand in candidates(a):
        if isGood(cand,a):
            a.append(cand)
            grid[leer[len(a)-1]] = cand
            back(a)
            grid[leer[len(a)-1]] = 0
            a.pop()
            
                
def isSolution(a):
    '''
    returns: True, wenn die Teillösung a eine Lösung darstellt
    '''
    return len(a) == anzahl

def candidates(a):
    '''
    returns: Liste von Entscheidungen, die die Teillösung a um eine Stufe erweitern
    '''
    return list(range(1,n+1))

def isGood(cand, a):
    '''
    returns: True, wenn die Entscheidung cand die Teillösung a sinnvoll erweitert.
    '''
    if len(a) >= anzahl: return False
    x, y = leer[len(a)]
    x1 = x//rn*rn
    y1 = y//rn*rn
    quadrat = grid[x1:x1+rn,y1:y1+rn].flatten()
    if cand not in grid[x,:] and cand not in grid[:,y] and cand not in quadrat:
        return True
    return False


n = 4
data = '''
.2..
1.4.
...3
3...
'''
import numpy as np
import math

data = data.replace('.', '0')
grid = np.array([int(x) for x in data if x.isdigit()]).reshape(n, n)
leer = list(zip(*np.where(grid == 0)))     # Koordinaten der Leerfelder
anzahl = len(leer)                         

# Eine Lösung besteht darin, die leeren Felder mit den Zahlen 1 bis 9 zu füllen.
# Eine Lösung a ist eine Liste der Länge anzahl, die die Zahlen für die leeren Felder enthält.
solutions = []
back([])
print(f'Anzahl der Lösungen: {len(solutions)}')

for i, solution in enumerate(solutions):
    grid0 = grid.copy()
    print(f'Lösung {i+1}:')
    for k in range(anzahl):
        x, y = leer[k]
        grid0[x, y] = solution[k]
    print(grid0)
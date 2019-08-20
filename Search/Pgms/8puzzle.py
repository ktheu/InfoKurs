# -*- coding: utf-8 -*-


import time
from collections import deque
from heapq import heappop, heappush

def reconstructPath(prev):
    '''
    prev: dictionary, das jeder Spielstellung ihren Vorgänger zuordnet.
       Die Startstellung hat als Vorgänger None zugeordnet.
    returns: tuple pfad, laenge
       pfad: String-Repräsentation des Weges von der Start- zur Zielstellung
       laenge: int, Länge des Weges in pfad
    '''
    s = (0,1,2,3,4,5,6,7,8)
    tmp = []
    while prev[s] is not None:
        i = s.index(0)
        ip = prev[s].index(0)
        if i == ip-1: tmp.append('left')
        elif i == ip+1: tmp.append('right')
        elif i == ip+3: tmp.append('down')
        elif i == ip-3: tmp.append('up')
        else: tmp.append('error')
        s = prev[s]
    tmp.reverse()
    return ' '.join(tmp),len(tmp)
    


def nextstates(state):
    '''
    state: Spielstellung
    returns: Liste mit den möglichen Folgestellungen für state. Die möglichen
       Bewegung des Leerfeldes halten sich an die Reihenfolge: up, down, left, right 
    '''
    if state[0] == 0:   return [swap(state,0,3),swap(state,0,1)]
    elif state[1] == 0: return [swap(state,1,4),swap(state,1,0),swap(state,1,2)]
    elif state[2] == 0: return [swap(state,2,5),swap(state,2,1)]
    elif state[3] == 0: return [swap(state,3,0),swap(state,3,6),swap(state,3,4)]
    elif state[4] == 0: return [swap(state,4,1),swap(state,4,7),swap(state,4,3),swap(state,4,5)]
    elif state[5] == 0: return [swap(state,5,2),swap(state,5,8),swap(state,5,4)]
    elif state[6] == 0: return [swap(state,6,3),swap(state,6,7)]
    elif state[7] == 0: return [swap(state,7,4),swap(state,7,6),swap(state,7,8)]
    elif state[8] == 0: return [swap(state,8,5),swap(state,8,7)]
    
def swap(state,i,j):
    ''' Hilfsfunktion für nextstates
    state: Spielstellung
    i, j: ints zwischen 0 und 8
    returns: Spielstellung, bei der gegenüber state die Zahlen an den
       Positionen i und j vertauscht sind.
    '''
    temp = list(state)
    temp[i],temp[j] = temp[j],temp[i]
    return tuple(temp)

def goaltest(state):
    '''
    state: Spielstellung
    returns: True, wenn state Zielposition ist
    '''
    return state == (0,1,2,3,4,5,6,7,8) 


def h1(state):
    '''
    state: Spielstellung
    returns Fortwärtskosten laut Heuristik
    '''
    return sum(a!=b for a,b in zip((0,1,2,3,4,5,6,7,8),state))//2 
      

def h(state): 
    '''
    state: Spielstellung
    returns: Fortwärtskosten laut Manhatten-Heuristik
    '''
    mh = 0
    for i in range(8):
        z1,s1 = i//3, i%3
        z2,s2 = state[i]//3, state[i]%3
        mh += abs(z1-z2)+abs(s1-s2)
    return mh//2

def bfs_long(s):
    frontier =  deque([s])
    prev = {s:None}
    nrExplored = 0
    explored = []
    while frontier:
        state = frontier.popleft()  
        explored.append(state)
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        for v in nextstates(state):
            if v not in frontier and v not in explored:
                frontier.append(v)
                prev[v] = state


               
def bfs(s):
    '''
    s: Startstellung
    returns: dictionary mit den Vorgängern der Spielstellungen auf dem
       Weg zum Ziel, None falls Ziel nicht gefunden
    '''
    '''
    In die frontier kommen alle rein, die wir noch untersuchen wollen.
    Wenn eine Spielstellung in die frontier kommt, merken wir uns gleichzeitig
    in einem dictionary den Vorgänger. Das dictionary bietet uns damit 
    gleichzeitig eine effiziente Möglichkeit zu testen, ob eine Stellung
    schon in der frontier ist. 
    
    '''
    frontier =  deque([s])
    prev = {s:None}
    nrExplored = 0
    while frontier:
        state = frontier.popleft()  
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state

def dfs(s):
    '''
    s: Startstellung
    returns: dictionary mit den Vorgängern der Spielstellungen auf dem
       Weg zum Ziel, None falls Ziel nicht gefunden
    '''
    frontier =  [s]
    prev = {s:None}
    nrExplored = 0
    while frontier:
        state = frontier.pop()  
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        nxt = nextstates(state)
        nxt.reverse()
        for v in nxt:
            if v not in prev:
                frontier.append(v)
                prev[v] = state

def greedy(s):
    '''
    s: Startstellung
    returns: dictionary mit den Vorgängern der Spielstellungen auf dem
       Weg zum Ziel, None falls Ziel nicht gefunden
    '''
    frontier =[(h(s),s)]  
    prev = {s:None}
    nrExplored = 0
    while frontier:
        _ ,state = heappop(frontier)  
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        for v in nextstates(state):
            if v not in prev:
                heappush(frontier,(h(v),v))
                prev[v] = state

def astar(s):
    '''
    s: Startstellung
    returns: dictionary mit den Vorgängern der Spielstellungen auf dem
       Weg zum Ziel, None falls Ziel nicht gefunden
    '''
    frontier =[(h(s),s)]  
    prev = {s:None}
    nrExplored = 0
    g = {s:0}  # backword costs: hier die Anzahl Züge
    while frontier:
        _ ,state = heappop(frontier)  # die Kosten braucht man an der Stelle nicht
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        for v in nextstates(state):
            if v not in prev:
                g[v] = g[state]+1
                heappush(frontier,(g[v]+h(v),v))
                prev[v] = state



#startstate = (3,1,2,0,4,5,6,7,8)
#startstate = (1,2,5,3,4,0,6,7,8)
#startstate = (6,2,5,8,7,4,1,0,3)
#startstate = (7,2,4,5,0,6,8,3,1)
#startstate = (1,4,2,3,7,5,6,0,8)
#startstate = (8,2,7,3,4,6,5,0,1)
startstate = (2,3,8,4,7,0,1,6,5)
start = time.perf_counter()
prev,nrExplored = astar(startstate) 
laufzeit = time.perf_counter()-start
pfad, laenge = reconstructPath(prev)
#print(pfad)
print('Länge = ',laenge)
print('#explored: ',nrExplored ,'Laufzeit:',laufzeit)     

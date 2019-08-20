G = {
'a': {'f':8, 'b':10},
'b': {'d':2},
'c': {'b':1},
'd': {'c':-2},
'e': {'d':-1,'b':-4},
'f': {'e':1}
}

def printNachbarn():
    for v in G:
        print('Nachbarn von',v,':',end=' ')
        for w in G[v]:
            print(w,'('+str(G[v][w])+')',end = ' ')
        print()
    print()

def printstatus(it):
    print(it,': ',end=' ')
    for v in sorted(G):
        print('{}'.format(dist[v]),end=' ')
    print()

def reconstructPath(s,u,prev):
    temp = []
    while u != s:
        temp.append(u)
        u = prev[u]
    temp.append(s)
    temp.reverse()
    return temp


printNachbarn()


inf = float('inf')
dist = {v:inf for v in G}
prev = {v:None for v in G}

s = 'a'         # startknoten
dist[s] = 0

changed = True
printstatus(0)
it = 1

while changed:
    changed = False
    for u in G:
        for v in G[u]:
            if dist[v] > dist[u] + G[u][v]:
                dist[v] = dist[u] + G[u][v]
                prev[v] = u
                changed = True
    printstatus(it)
    it+=1

print()
for v in G:
    print('Weg von {} zu {} : {:10s} - Entfernung: {:2}'.format(s,v,' '.join(reconstructPath(s,v,prev)),dist[v]))

G = {
'a': {'b':4, 'c':3},
'b': {'c':-2, 'd':4},
'c': {'d':-3, 'e':1},
'd': {'e':2},
'e': {}
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
        print('{:}:{:}'.format(v,dist[v]),end=' ')
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

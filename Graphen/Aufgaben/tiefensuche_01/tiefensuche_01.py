# -*- coding: utf-8 -*-
def zeigeNachbarn():
    for v in G:
        print('Nachbarn von',v,':',end=' ')
        for w in G[v]:
            print(w,'('+str(G[v][w])+')',end = ' ')
        print()

def explore(v):
    visited[v] = True
    for w in G[v]:
        ausgangskosten[v] += G[v][w]
    for w in G[v]:
        if not visited[w]:
            explore(w)

G = {
'a': {'b':2,'d':3},
'b': {'c':3, 'e':4},
'c': {'e':2},
'd': {'f':7},
'e': {'f':1},
'f': {}
}

visited = {v : False for v in G}
ausgangskosten = {v: 0 for v in G}
for w in G:
    if not visited[w]:
        explore(w)

for v in G:
    print(v,ausgangskosten[v])

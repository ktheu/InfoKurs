# -*- coding: utf-8 -*-
def zeigeNachbarn():
    for v in G:
        print('Nachbarn von',v,':',end=' ')
        for w in G[v]:
            print(w,'('+str(G[v][w])+')',end = ' ')
        print()

def explore(v):
    visited[v] = True
    min_kosten = inf
    min_knoten = None
    for w in G[v]:
        if G[v][w] < min_kosten:
            min_kosten = G[v][w]
            min_knoten = w
    min_nachbar[v] = min_knoten
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

inf = float('inf')
visited = {v : False for v in G}
min_nachbar = {v: None for v in G}
for w in G:
    if not visited[w]:
        explore(w)

for v in G:
    print(v,min_nachbar[v])

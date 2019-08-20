# -*- coding: utf-8 -*-

def explore(v):
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            parent[w] = v
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
parent = {v : None for v in G}
for w in G:
    if not visited[w]:
        explore(w)

print(parent)

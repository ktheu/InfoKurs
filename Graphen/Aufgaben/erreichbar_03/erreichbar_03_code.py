# -*- coding: utf-8 -*-
G = {
    'a': set('d'),
    'b': set('ce'),
    'c': set('b'),
    'd': set('a'),
    'e': set('bf'),
    'f': set('e')
}

def explore(v):
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            explore(w)

nb = G['b']
print('Nachbarn von b:',*nb)

visited = {v : False for v in G}
explore('b')
eb = [v for v in G if visited[v]]
print('Erreichbar von b:',*eb)

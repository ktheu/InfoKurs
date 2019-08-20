# -*- coding: utf-8 -*-

def explore(v):
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            explore(w)
G = {
    'a': set('e'),
    'b': set('e'),
    'c': set('d'),
    'd': set('c'),
    'e': set('abf'),
    'f': set('e')

}


for w in G:
    visited = {v : False for v in G}
    explore(w)
    result = [v for v in G if visited[v]]
    print('Erreichbar von',w,':',*result)

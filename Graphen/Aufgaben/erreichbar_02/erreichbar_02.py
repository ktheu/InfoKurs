# -*- coding: utf-8 -*-

def explore(v):
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            explore(w)

G = {
    'a': set('cdf'),
    'b': set('e'),
    'c': set('aih'),
    'd': set('a'),
    'e': set('bjg'),
    'f': set('ai'),
    'g': set('e'),
    'h': set('ci'),
    'i': set('cfh'),
    'j': set('e')
}

for w in G:     
    visited = {v : False for v in G}  
    explore(w)      
    result = [v for v in G if visited[v]]            
    print('Erreichbar von',w,':',*result)

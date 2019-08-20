# -*- coding: utf-8 -*-
'''
Der kürzeste Weg in einem ungewichteten Graphen mittels Breitensuche
'''
G = {
'a': set('bc'),
'b': set('aed'),
'c': set('aef'),
'd': set('bg'),
'e': set('bcfg'),
'f': set('cei'),
'g': set('dehj'),
'h': set('geik'),
'i': set('fhm'),
'j': set('gk'),
'k': set('jhm'),
'm': set('ki')
}

def reconstructPath(s,u,prev):
    result = []
    while u != s:
        result.append(u)
        u = prev[u]
    result.append(s)
    result.reverse()
    return result
        
inf = float('inf')
dist = {v:inf for v in G}
prev = {v:None for v in G}

s = 'a'         # Startknoten
dist[s] = 0     
Q = [s]         # Queue mit pop(0) und append
while Q:
    u = Q.pop(0)
    for v in sorted(G[u]):
        if dist[v] == inf:
            Q.append(v)
            dist[v] = dist[u]+1
            prev[v] = u
ziel = 'k'            
print('Pfad von',s,'nach',ziel,':',*reconstructPath(s,ziel,prev))
print('Länge =',dist[ziel])

for v in G:
    nachfolger = [w for w in G if prev[w]== v]
    if len(nachfolger) > 0:
        print('Kind von',v,':',nachfolger)

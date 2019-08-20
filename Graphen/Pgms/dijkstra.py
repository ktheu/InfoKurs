# -*- coding: utf-8 -*-

'''
Single source shortest path: Der Algorithmus von Dijkstra
'''
from heapq import heapify, heappop, heappush

G = {
'a': {'b':2, 'c':9},
'b': {'c':5, 'd':13},
'c': {'d':6, 'e':9},
'd': {'e':1, 'f':5},
'e': {'f':2},
'f': {}
}

def reconstructPath(s,u,prev):
    temp = []
    while u != s:
        temp.append(u)
        u = prev[u]
    temp.append(s)
    temp.reverse()
    return temp

inf = float('inf')
dist = {v:inf for v in G}
prev = {v:None for v in G}

start, ziel = 'a', 'f'
dist[start] = 0
visited = set()

heap = [(dist[v],v) for v in G]
heapify(heap)

while heap:
    _, u = heappop(heap)
    if u in visited: continue
    visited.add(u)
    for v in G[u]:
        if dist[v] > dist[u] + G[u][v]:
            dist[v] = dist[u] + G[u][v]
            prev[v] = u
            heappush(heap,(dist[v],v))

print('Pfad von',start,'nach',ziel,':',*reconstructPath(start,ziel,prev))
print('Distanz:',dist[ziel])

# -*- coding: utf-8 -*-

'''
Single source shortest path: Der Algorithmus von Dijkstra
'''
from heapq import heapify, heappop, heappush

G = {
'a': {'b':3, 'c':10}, 
'b': {'c':8, 'd':3, 'e':5}, 
'c': {'b':2, 'e':5}, 
'd': {'c':3, 'e':1, 'f':2},  
'e': {'f':0}, 
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

s = 'a'         # startknoten
dist[s] = 0
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
ziel = 'f'
print('Pfad von',s,'nach',ziel,':',*reconstructPath('a','f',prev))
print('Distanz:',dist[ziel])

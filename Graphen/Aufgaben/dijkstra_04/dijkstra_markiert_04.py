# -*- coding: utf-8 -*-

'''
Single source shortest path: Der Algorithmus von Dijkstra
'''
from heapq import heapify, heappop, heappush

G = {
'a': {'b':2, 'c':6}, 
'b': {'c':3,'d':5}, 
'c': {'d':1}, 
'd': {}  
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

endgueltig = [] 
markierung = {v:'inf' for v in G}
markierung[s]='0'
while heap:
    _, u = heappop(heap)
    if u in visited: continue
    visited.add(u)
    endgueltig.append(u)
    for v in G[u]:
        if dist[v] > dist[u] + G[u][v]:
            dist[v] = dist[u] + G[u][v]
            print(v,markierung[v])
            markierung[v] = markierung[v] + ' ' + str(dist[v])
            prev[v] = u
      
            heappush(heap,(dist[v],v))
for v in G:
    print('Entfernung zu',v,':',dist[v])
print('Endgültig markiert:',*endgueltig)
for m in markierung:
    print(m,':',markierung[m])
# -*- coding: utf-8 -*-

'''
Single source shortest path: Der Algorithmus von Dijkstra
'''
from heapq import heapify, heappop, heappush

G = {
'a': {'b':10, 'c':1, 'f': 5}, 
'b': {}, 
'c': {'b':8, 'd':1, 'f':3}, 
'd': {'b':6, 'e':3},  
'e': {'b':2}, 
'f': {'b':6, 'd':1} 
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
# -*- coding: utf-8 -*-

def explore(v):
    visited[v] = True
    ccnum[v] = cc
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

visited = {v : False for v in G}  
ccnum = {v : 0 for v in G}          # connected component nr of v
cc = 1

for v in G.keys():
    if not visited[v] :
        explore(v)
        cc+=1
      
for i in range(1,cc):
    result = [v for v in G if visited[v] and ccnum[v] == i]    
    print(i,'-',*result)
    
'''
Ausgabe: 
1 - a b e f
2 - c d
'''
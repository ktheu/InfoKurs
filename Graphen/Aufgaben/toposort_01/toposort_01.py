# -*- coding: utf-8 -*-
def explore(v):
    global counter
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            explore(w)
    postvisit[v] = counter
    counter += 1

G = {
'a': set('c'),
'b': set('c'),
'c': set('d'),
'd': set('g'),
'e': set('df'),
'f': set('g'),
'g': set()
}

visited = {v : False for v in G}
postvisit = {v : 0 for v in G}
counter = 1

for v in G:
    if not visited[v] :
        explore(v)

topolist = sorted(G.keys(),key=lambda v: postvisit[v],reverse = True)
for i in range(len(topolist)):
    print(i+1,topolist[i])

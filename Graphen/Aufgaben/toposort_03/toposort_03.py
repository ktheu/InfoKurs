# -*- coding: utf-8 -*-
def explore(v):
    global counter
    previsit[v] = counter
    counter += 1
    visited[v] = True
    for w in sorted(G[v]):
        if not visited[w]:
            explore(w)
    postvisit[v] = counter
    counter += 1

G = {
'a': set('d'),
'b': set('ed'),
'c': set('d'),
'd': set('f'),
'e': set('h'),
'f': set('h'),
'g': set('e'),
'h': set()
}

visited = {v : False for v in G}
postvisit = {v : 0 for v in G}
previsit = {v : 0 for v in G}
counter = 1

for v in sorted(G):
    if not visited[v] :
        explore(v)

topolist = sorted(G,key=lambda v: postvisit[v],reverse = True)
for i in range(len(topolist)):
    v = topolist[i]
    print(i+1,v,previsit[v],postvisit[v])

print(*topolist)

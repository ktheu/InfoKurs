# -*- coding: utf-8 -*-
def explore(v):
    global counter
    visited[v] = True
    previsit[v] = counter
    counter += 1
    for w in sorted(G[v]):  #  alphabetische Reihenfolge
        if not visited[w]:
            explore(w)
    postvisit[v] = counter
    counter += 1

G = {
'a': set('bde'),
'b': set('ae'),
'c': set('gi'),
'd': set('ah'),
'e': set('abf'),
'f': set('eh'),
'g': set('ci'),
'h': set('df'),
'i': set('cg'),
}

visited = {v : False for v in G}
previsit = {v : 0 for v in G}
postvisit = {v : 0 for v in G}

counter = 1
for v in G:
    if not visited[v] :
        explore(v)

for v in sorted(G,key=lambda v: previsit[v]):
    print("{:2} {:1} {:2}".format(v,previsit[v],postvisit[v]))

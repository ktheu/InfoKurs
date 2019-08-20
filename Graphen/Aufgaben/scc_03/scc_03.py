# -*- coding: utf-8 -*-
G = {
'a': set('b'),
'b': set('cf'),
'c': set('a'),
'd': set('f'),
'e': set('g'),
'f': set('e'),
'g': set('dh'),
'h': set('j'),
'j': set('i'),
'i': set('j')
}
# explore reverse Graph, merke postvisit nr
# und previsit nr
def exploreR(v):
    global counter
    previsit[v] = counter
    counter += 1
    visited[v] = True
    for w in sorted(Gr[v]):
        if not visited[w]:
            exploreR(w)
    postvisit[v] = counter
    counter+=1

# explore Graph, merke connected component number
def explore(v):
    visited[v] = True
    ccnum[v] = cc
    for w in G[v]:
        if not visited[w]:
            explore(w)


# Gr ist der reverse Graph von G
Gr = {v:set() for v in G}
for v in G:
    for w in G[v]:
        Gr[w].add(v)

# dfs durch den reversen Graphen, merke previsit/ postvisit-nr
visited = {v : False for v in Gr}
previsit = {v : 0 for v in Gr}
postvisit = {v : 0 for v in Gr}
counter = 1
for v in sorted(Gr):
    if not visited[v] :
        exploreR(v)

# die Knoten in der umgekehrten postvisit-Reihenfolge des reversen Graphen
vlist = sorted(Gr,key=lambda v: postvisit[v],reverse=True)
print('Die Reihenfolge, in der die Knoten besucht werden')
print(*vlist)
print('Die pre/post-visit-Nummern des transponierten Graphen')
for v in vlist:
    print(v,previsit[v],postvisit[v])

print()


# dfs durch den Ausgangsgraphen, in der vlist Reihenfolge, dabei component nr merken
visited = {v : False for v in G}
ccnum = {v : 0 for v in G}
cc = 1
for v in vlist:
    if not visited[v] :
        explore(v)
        cc+=1

# Ausgabe
for i in range(1,cc):
    result = sorted([v for v in G if ccnum[v] == i])
    print(i,'-',*result)

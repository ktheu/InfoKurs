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
'a': set('bcd'),
'b': set('ac'),
'c': set('ab'),
'd': set('a'),
'e': set('f'),
'f': set('e'),
'g': set('hi'),
'h': set('gi'),
'i': set('gh'),
}


visited = {v : False for v in G}
previsit = {v : 0 for v in G}
postvisit = {v : 0 for v in G}
counter = 1

for v in G.keys():
    if not visited[v] :
        explore(v)

for v in sorted(G,key=lambda v: previsit[v]):
    print("{:2} {:2} {:2}".format(v,previsit[v],postvisit[v]))

'''
a   1  8
b   2  5
c   3  4
d   6  7
e   9 12
f  10 11
g  13 18
h  14 17
i  15 16
'''

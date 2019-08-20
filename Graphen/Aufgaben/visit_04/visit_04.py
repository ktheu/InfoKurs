# -*- coding: utf-8 -*-

def printNachbarn():
    for v in G:
        print('Nachbarn von',v,':',end=' ')
        print(*sorted(G[v]))


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
'b': set('ced'),
'c': set('b'),
'd': set('abf'),
'e': set('ab'),
'f': set('d'),
}

printNachbarn()

visited = {v : False for v in G}
previsit = {v : 0 for v in G}
postvisit = {v : 0 for v in G}

counter = 1
for v in G:
    if not visited[v] :
        explore(v)

for v in sorted(G,key=lambda v: previsit[v]):
    print("{:2} {:1} {:2}".format(v,previsit[v],postvisit[v]))

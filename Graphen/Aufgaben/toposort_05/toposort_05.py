# -*- coding: utf-8 -*-
def printNachbarn():
    for v in G:
        print('Nachbarn von',v,':',end=' ')
        print(*sorted(G[v]))


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
'a': set('e'),
'b': set('de'),
'c': set('eh'),
'd': set('g'),
'e': set('gh'),
'f': set('ei'),
'g': set('h'),
'h': set('i'),
'i': set()
}

visited = {v : False for v in G}
postvisit = {v : 0 for v in G}
previsit = {v : 0 for v in G}
counter = 1

for v in sorted(G):
    if not visited[v] :
        explore(v)

printNachbarn()

topolist = sorted(G,key=lambda v: postvisit[v],reverse = True)
for i in range(len(topolist)):
    v = topolist[i]
    print(i+1,v,previsit[v],postvisit[v])

print(*topolist)

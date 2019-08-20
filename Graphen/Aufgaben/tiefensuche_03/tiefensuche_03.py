# -*- coding: utf-8 -*-
def zeigeNachbarn():
    for v in G:
        print('Nachbarn von',v,':',end=' ')
        for w in G[v]:
            print(w,'('+str(G[v][w])+')',end = ' ')
        print()

def explore(v):
    bknoten.add(v)
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            explore(w)

G = {
'a': {'b':2,'d':3},
'b': {'c':3, 'e':4},
'c': {'e':2},
'd': {'f':7},
'e': {'f':1},
'f': {}
}


inf = float('inf')
visited = {v : False for v in G}
bknoten = set()
explore('b')

print(bknoten)


bknoten1 = set()
visited1 = [False for x in G.keys()]
def explore1(s):
    visited1[ord(s)-97] = True
    for i in range(len(G[ord(s)-97])):
        explore1(G[ord(s-97)][i])
        
explore1('b')
                   
# -*- coding: utf-8 -*-

G = {
'a': {'c':7, 'b':4, 'd':12},
'b': {'c':1},
'c': {'d':3},
'd': {},
}


for v in G:
    print('Nachbarn von',v,':',end=' ')
    for w in G[v]:
        print(w,'('+str(G[v][w])+')',end = ' ')
    print()

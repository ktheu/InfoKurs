# -*- coding: utf-8 -*-

G = {
'a': {'c':4, 'd':2},
'b': {'a':3},
'c': {'a':1, 'd':5},
'd': {},
}


for v in G:
    print('Nachbarn von',v,':',end=' ')
    for w in G[v]:
        print(w,'('+str(G[v][w])+')',end = ' ')
    print()

# -*- coding: utf-8 -*-

G = {
'a': {'b':3, 'c':1},
'b': {'c':4, 'd':5},
'c': {},
'd': {'a':2},
}


for v in G:
    print('Nachbarn von',v,':',end=' ')
    for w in G[v]:
        print(w,'('+str(G[v][w])+')',end = ' ')
    print()

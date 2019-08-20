# -*- coding: utf-8 -*-

G = {
'a': {'b':2, 'c':9},
'b': {'c':5, 'd':13},
'c': {'d':6, 'e':9},
'd': {'e':1, 'f':5},
'e': {'f':2},
'f': {}
}


for v in G:
    print('Nachbarn von',v,':',end=' ')
    for w in G[v]:
        print(w,'('+str(G[v][w])+')',end = ' ')
    print()

'''
Nachbarn von a : b (2) c (9)
Nachbarn von b : c (5) d (13)
Nachbarn von c : d (6) e (9)
Nachbarn von d : e (1) f (5)
Nachbarn von e : f (2)
Nachbarn von f : 
'''

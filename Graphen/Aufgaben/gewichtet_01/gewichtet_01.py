# -*- coding: utf-8 -*-

G = {
  'a': {'b':1, 'c':3, 'd':4},
  'b': {'c':5},
  'c': {'d':2},
  'd': {}
}

for v in G:
    print('Nachbarn von',v,':',end=' ')
    for w in G[v]:
        print(w,'('+str(G[v][w])+')',end = ' ')
    print()
        

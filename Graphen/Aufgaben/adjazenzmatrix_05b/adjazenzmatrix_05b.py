# -*- coding: utf-8 -*-
inf = float('inf')
G = [[0,inf,4,1],
     [3,0,inf,5],
     [inf,inf,0,2],
     [inf,2,inf,0]]

n = len(G)
for x in range(n):
    nb = [chr(y+97) for y in range(n) if x != y and G[x][y]  < inf ]
    print('Nachbarn von',chr(x+97),end=': ')
    for w in nb:
        print(w,G[x][ord(w)-97],end=' ')
    print()

# -*- coding: utf-8 -*-
inf = float('inf')
G = [[0,inf,2,3],
     [inf,0,1,inf],
     [inf,inf,0,2],
     [inf,inf,4,0]]

n = len(G)
for x in range(n):
    nb = [chr(y+97) for y in range(n) if x != y and G[x][y]  < inf ]
    print('Nachbarn von',chr(x+97),end=': ')
    for w in nb:
        print(w,G[x][ord(w)-97],end=' ')
    print()

# Gib den Kopf einer for-Schleife an, die durch alle Nachbarn von b läuft
nb = [chr(y+97) for y in range(len(G)) if y != 0 and G[0][y] < inf]
print(*nb)

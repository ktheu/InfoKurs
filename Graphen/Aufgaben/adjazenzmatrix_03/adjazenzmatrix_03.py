# -*- coding: utf-8 -*-
inf = float('inf')

G = [[0, 3, inf, 9],
     [inf, 0, 2, inf],
     [inf, inf, 0, inf],
     [8, 4, 5, 0]]

n = len(G)
for x in range(n):
    nb = [chr(y+97) for y in range(n) if x != y and G[x][y] < inf]
    print('Nachbarn von',chr(x+97),':',*nb)

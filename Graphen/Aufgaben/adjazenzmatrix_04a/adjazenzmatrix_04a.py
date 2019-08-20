# -*- coding: utf-8 -*-
G = [[0,1,1,0],
     [1,0,1,0],
     [1,1,0,1],
     [0,0,1,0]]

n = len(G)
for x in range(n):
    nb = [chr(y+97) for y in range(n) if G[x][y]]
    print('Nachbarn von',chr(x+97),':',*nb)

# Alle Nachbarn von c
nb = [chr(y+97) for y in range(len(G)) if G[2][y]]
print(*nb)

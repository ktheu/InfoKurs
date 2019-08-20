# -*- coding: utf-8 -*-
G = [[0,1,1,0,0],
     [1,0,1,0,1],
     [1,1,0,1,0],
     [0,0,1,0,1],
     [0,1,0,1,0]]

n = len(G)
for x in range(n):
    nb = [chr(y+97) for y in range(n) if G[x][y]]
    print('Nachbarn von',chr(x+97),':',*nb)

# Gib den Kopf einer for-Schleife an, die durch alle Nachbarn von b läuft
nb = [chr(y+97) for y in range(len(G)) if G[1][y]]
print(*nb)

# Welcher Ausdruck prüft, ob d ein Nachbar von a ist?

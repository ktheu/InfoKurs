# -*- coding: utf-8 -*-

G = [[0,1,1,0,0],
     [1,0,1,0,1],
     [1,1,0,1,0],
     [0,0,1,0,1],
     [0,1,0,1,0]]

# Gib den Kopf einer for-Schleife an, die durch alle Nachbarn von b läuft
nb = [chr(y+97) for y in range(len(G)) if G[1][y]]
print(*nb)

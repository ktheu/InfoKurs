# -*- coding: utf-8 -*-
inf = float('inf')

G = [[0, 0, 1, 1, 1, 0],
     [0, 0, 1, 0, 1, 1],
     [1, 1, 0, 0, 1, 1],
     [1, 0, 0, 0, 0, 1],
     [1, 1, 1, 0, 0, 0],
     [0, 1, 1, 1, 0, 0]]

n = len(G)
for x in range(n):
    nb = [chr(y+97) for y in range(n) if G[x][y]]
    print('Nachbarn von',chr(x+97),':',*nb)


'''
Nachbarn von a : c d e
Nachbarn von b : c e f
Nachbarn von c : a b e f
Nachbarn von d : a f
Nachbarn von e : a b c
Nachbarn von f : b c d
'''

# -*- coding: utf-8 -*-
inf = float('inf')
G = [[0,inf,2,5],
     [4,0,1,inf],
     [3,inf,0,inf],
     [inf,inf,inf,0]]

nb = [chr(y+97) for y in range(len(G)) if y != 0 and G[1][y] < inf]
print(*nb)

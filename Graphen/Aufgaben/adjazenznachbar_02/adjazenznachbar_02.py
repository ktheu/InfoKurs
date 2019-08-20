# -*- coding: utf-8 -*-
inf = float('inf')
G = [[0,inf,1,3],
     [inf,0,1,inf],
     [inf,inf,1,2],
     [inf,inf,4,0]]


nb = [chr(y+97) for y in range(len(G)) if y != 0 and G[0][y] < inf]
print(*nb)

# -*- coding: utf-8 -*-
inf = float('inf')
graph = [[0,inf,2,5],
     [4,0,1,inf],
     [3,inf,0,inf],
     [inf,inf,inf,0]]


nb = [chr(y+97) for y in range(len(graph)) if (y != 2 and graph[2][y] < inf)]
print(*nb)

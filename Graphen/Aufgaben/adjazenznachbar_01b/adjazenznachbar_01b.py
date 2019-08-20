# -*- coding: utf-8 -*-

graph = [[0,1,1,0,0],
     [1,0,1,0,1],
     [1,1,0,1,0],
     [0,0,1,0,1],
     [0,1,0,1,0]]

nb = [chr(y+97) for y in range(len(graph)) if graph[3][y]]
print(*nb)

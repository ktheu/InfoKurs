import sys
sys.setrecursionlimit(10000000)
 
def dfs(v):  
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfs(w) 

# einlesen und grid erstellen
hoehe, breite = [int(x) for x in input().split()]
grid = []
for _ in range(hoehe):
    grid.append(list(input()))

V = [(x,y) for x in range(hoehe) for y in range(breite) if grid[x][y] != '#']
G = {v: set() for v in V}
 

# Graph erstellen
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
for v in G:
    x, y = v
    for xd, yd in dirs:
        x1, y1 = x+xd, y+yd
        if 0 <= x1 < hoehe and 0 <= y1 < breite and grid[x1][y1] != '#':
            G[v].add((x1,y1))

zaehl = 0
visited =  {v : False for v in G}     
for v in G:
    if not visited[v]:
        zaehl+=1
        dfs(v)
print(zaehl)   

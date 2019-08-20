G = {
  'a': {'b':4, 'f':12, 'g':7},
  'b': {'c':3, 'g':2},
  'c': {'d':4, 'g':4},
  'd': {},
  'e': {'d':10},
  'f': {'e':9, 'g':7},
  'g': {'d':6, 'e':11}
}

def minus(G):
    Gm = {}
    for v in G:
        dict = {}
        for k in G[v]:
            dict[k] = - G[v][k]
        Gm[v] = dict
    return Gm

Gm = minus(G)

def reconstructPath(s,u,prev):
    temp = []
    while u != s:
        temp.append(u)
        u = prev[u]
    temp.append(s)
    temp.reverse()
    return temp

inf = float('inf')
dist = {v:inf for v in Gm}
prev = {v:None for v in Gm}

start, ziel = 'a' , 'd'
dist[start] = 0

changed = True
while changed:
    changed = False
    for u in Gm:
        for v in Gm[u]:
            if dist[v] > dist[u] + Gm[u][v]:
                dist[v] = dist[u] + Gm[u][v]
                prev[v] = u
                changed = True

print('laengster Pfad von',start,'nach',ziel,':',*reconstructPath(start,ziel,prev))
print('Distanz:',-dist[ziel])
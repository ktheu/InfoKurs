G = {
'a': {'b':4, 'c':3},
'b': {'c':-2, 'd':4},
'c': {'d':-3, 'e':1},
'd': {'e':2},
'e': {}
}

def reconstructPath(s,u,prev):
    temp = []
    while u != s:
        temp.append(u)
        u = prev[u]
    temp.append(s)
    temp.reverse()
    return temp

inf = float('inf')
dist = {v:inf for v in G}
prev = {v:None for v in G}

start, ziel = 'a' , 'd'
dist[start] = 0

changed = True
while changed:
    changed = False
    for u in G:
        for v in G[u]:
            if dist[v] > dist[u] + G[u][v]:
                dist[v] = dist[u] + G[u][v]
                prev[v] = u
                changed = True

print('Pfad von',start,'nach',ziel,':',*reconstructPath(start,ziel,prev))
print('Distanz:',dist[ziel])

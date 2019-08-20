'''
Minimaler Spannbaum (Minimum Spanning Tree, MST): der Algorithmus von Kruskal
'''
G = {
  'a': {'b':5, 'c':6, 'd':4, 'f':3},
  'b': {'a':5, 'c':9, 'd':6, 'e':7},
  'c': {'a':6, 'b':9, 'e':8, 'h':7},
  'd': {'a':4, 'b':6, 'f':5, 'g':6},
  'e': {'b':7, 'c':8, 'g':8, 'h':9},
  'f': {'a':3, 'd':5, 'g':2, 'h':1},
  'g': {'d':6, 'e':8, 'f':2, 'h':4},
  'h': {'f':1, 'g':4, 'e':9, 'c':7}
}

def printMst(mst):
    for u,v in mst:
        print('{}-{} ({}),'.format(u,v,G[u][v]), end=' ')

def find(u):                           # finde chef
    while chef[u] != u:                # chef zeigt auf sich selbst
        u = chef[u]
    return u

def union(u, v):
    u = find(u)                        # finde beide chefs
    v = find(v)
    chef[u] = v                        # der eine zeigt auf den anderen
    print('Chef von',u,'wird',v)

zaehler = 1
summe = 0
gesehen = set()
E = []
for u in G:
    for v in G[u]:
        if (u,v) not in gesehen:
            if u < v:
                E.append((G[u][v],u,v))
            else:
                E.append((G[v][u],v,u))
            gesehen.add((u,v))
            gesehen.add((v,u))



  # Kantenliste mit Kosten
E = sorted(E)                                   # nach Kosten sortieren
mst = []                                        # leere Teillösung
chef = {u:u for u in G}                         # zunächst ist jeder eigener chef
for _, u, v in sorted(E):
    if find(u) != find(v):                      # wenn chefs verschieden,
        mst.append((u, v))
        print(u + '-' + v + ':',G[u][v])
        zaehler+=1                    # vereinige
        summe += G[u][v]
        union(u, v)
    else:
        print('{} und {} haben gleiche Chefs'.format(u,v))

printMst(mst)
print('Gesamtkosten: ', summe)
print()
print('Chefbaum:')
print(chef)

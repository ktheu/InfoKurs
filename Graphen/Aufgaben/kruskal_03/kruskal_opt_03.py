'''
Minimaler Spannbaum (Minimum Spanning Tree, MST): der Algorithmus von Kruskal
'''
G = {
  'a': {'b':7, 'd':5},
  'b': {'a':7, 'd':9, 'e':7, 'c':8},
  'c': {'b':8, 'e':5},
  'd': {'a':5, 'b':9, 'e':15, 'f':6},
  'e': {'b':7, 'c':5, 'd':15, 'f':8, 'g':9},
  'f': {'d':6, 'e':8, 'g':11},
  'g': {'e':9, 'f':11}
}

def printMst(mst):
    for u,v in mst:
        print('{}-{} ({}),'.format(u,v,G[u][v]), end=' ')

def find(u):                           # finde chef
    if chef[u] != chef[chef[u]]:
        chef[u] = find(chef[u])        # Path compression
        print('Kompression: Chef von',u,'wird',chef[u])
    return chef[u]

# def find(u):
#     root = u                         # finde chef
#     while chef[root] != root:                # chef zeigt auf sich selbst
#         root = chef[root]
#         #print('Chef von ',u,'gefunden:',root)
#
#     while chef[u] != root:
#         chef[u] = root
#         print('Pathcompression: Chef von',u,'wird',root)
#         u = chef[u]
#     return root

def union(u, v):
    u = find(u)                        # finde beide chefs
    v = find(v)
    if rank[u] > rank[v]:
        chef[v] = u
        print('Rang',u,'größer Rang',v,': Chef von',v,'wird',u)
    else:
        chef[u] = v
        if rank[u] < rank[v]:
            print('Rang',u,'kleiner Rang',v,': Chef von',u,'wird',v)
        elif rank[u] == rank[v]:
            print('Rang',u,'gleich Rang',v,': Chef von',u,'wird',v)
    if rank[u] == rank[v]:             # bei gleichem rang wird v chef
        rank[v]+=1
        print('Rang von',v,'wird',rank[v])




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
rank = {u:0 for u in G}
for _, u, v in sorted(E):
    if find(u) != find(v):                      # wenn chefs verschieden,
        mst.append((u, v))
        print(u + '-' + v + ':',G[u][v],' ',end=' ')
        zaehler+=1                    # vereinige
        summe += G[u][v]
        union(u, v)
    else:
        pass
        #print('{} und {} haben gleiche Chefs'.format(u,v))

printMst(mst)
print('Gesamtkosten: ', summe)
print()
print('Chefbaum:')
print(chef)

'''
Minimaler Spannbaum (Minimum Spanning Tree, MST): der Algorithmus von Kruskal
optimierte Version
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
    '''
    printed die kanten des mst in der reihenfolge des einfügens,
    jeweils alphabetische Reihenfolge der Knoten.
    '''
    for u,v in mst:
        print('{}-{}'.format(u,v), end=' ')

# def find(u):                           # finde chef
#     if chef[u] != chef[chef[u]]:
#         chef[u] = find(chef[u])        # Path compression
#         print('Kompression: Chef von',u,'wird',chef[u])
#     return chef[u]

def find(u):
    root = u                         # finde chef
    while chef[root] != root:        # chef zeigt auf sich selbst
        root = chef[root]
    while chef[u] != root:           # Path compression
        chef[u] = root
        print('Kompression: Chef von',u,'wird',chef[u])
        u = chef[u]
    return root

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

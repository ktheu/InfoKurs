'''
Minimaler Spannbaum (Minimum Spanning Tree, MST): der Algorithmus von Kruskal
'''
G = {
  'a': {'b':5, 'd':9, 'e':1},
  'b': {'a':5, 'c':4, 'd':2},
  'c': {'h':4, 'b':4, 'i':1, 'j':8},
  'd': {'a':9, 'b':2, 'h':2, 'g':11, 'f':5, 'e':2},
  'e': {'a':1, 'd':2, 'f':1},
  'f': {'e':1, 'd':5, 'g':7},
  'g': {'f':7, 'd':11, 'h':1, 'i':4},
  'h': {'d':2, 'c':4, 'i':6, 'g':1},
  'i': {'g':4, 'h':6, 'c':1, 'j':0},
  'j': {'c':8, 'i':0}
}

def printNachbarn():
    for v in G:
        print('Nachbarn von',v,':',end=' ')
        for w in G[v]:
            print(w,'('+str(G[v][w])+')',end = ' ')
        print()

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

printNachbarn()
print()
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

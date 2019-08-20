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

def find(u):
    if chef[u] != chef[chef[u]]:
        chef[u] = find(chef[u])        # Path compression
    return chef[u]

def union(u, v):                       # union by rank
    u, v = find(u), find(v)
    if rank[u] > rank[v]:
        chef[v] = u
    else:
        chef[u] = v
    if rank[u] == rank[v]:
        rank[v]+=1

summe = 0
gesehen = set()

E = [(G[u][v],u,v) for u in G for v in G[u]]  # Kantenliste mit Kosten

mst = []                             # leere Anfangsbaum
chef = {u:u for u in G}              # zunächst ist jeder eigener chef
rank = {u:0 for u in G}              # und hat Rang 0
for _, u, v in sorted(E):
    if find(u) != find(v):           # wenn chefs verschieden, wird die
        mst.append((u, v))           # Kante in den mst aufgenommen
        summe += G[u][v]
        union(u, v)

print(mst)
print('Gesamtkosten: ', summe)

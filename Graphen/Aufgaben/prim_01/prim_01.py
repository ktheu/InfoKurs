from heapq import heappop, heappush

G = {
  'a': {'b':7, 'd':5},
  'b': {'a':7, 'd':9, 'e':7, 'c':8},
  'c': {'b':8, 'e':5},
  'd': {'a':5, 'b':9, 'e':15, 'f':6},
  'e': {'b':7, 'c':5, 'd':15, 'f':8, 'g':9},
  'f': {'d':6, 'e':8, 'g':11},
  'g': {'e':9, 'f':11}
}

start = 'a'                              # Startknoten
mst = {}                                 # leere Teillösung
heap = [(0, None, start)]                # Heap mit Kanten und Kosten
summe = 0
kantenreihenfolge = ''
while heap:
    cost, prev, u = heappop(heap)
    if u in mst: continue            # Zielknoten schon im Baum?
    mst[u] = prev                    # Kante von u nach prev kommt in mst
    if prev is not None:
        kantenreihenfolge += prev+'-'+u+', '
    summe += cost
    for v, cost in G[u].items():
        heappush(heap, (cost, u, v))
print(kantenreihenfolge[:-2])
print(mst)
print('Gesamtkosten: ', summe)
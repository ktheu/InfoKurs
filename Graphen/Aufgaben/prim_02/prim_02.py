from heapq import heappop, heappush

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
from heapq import heappop, heappush

G = {
  'a': {'b':5, 'd':3, 'e':6},
  'b': {'a':5, 'c':4},
  'c': {'h':4, 'b':4, 'i':1, 'j':8, 'd':3},
  'd': {'a':3, 'c':3, 'h':2, 'g':11,  'e':2},
  'e': {'a':6, 'd':2, 'f':1, 'g':3},
  'f': {'e':1, 'g':7},
  'g': {'f':7, 'd':11, 'e':3, 'h':2, 'i':4},
  'h': {'d':2, 'c':4, 'i':6, 'g':2},
  'i': {'g':4, 'h':6, 'c':1, 'j':4},
  'j': {'c':8, 'i':4}
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

from heapq import heappop, heappush
a = ['lena','maike','thorben']
b = [(len(x),x) for x in a]
hp = []
for s in b:
    heappush(hp,s)

while hp:
    print(heappop(hp))

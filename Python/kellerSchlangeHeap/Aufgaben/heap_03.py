from heapq import heappop, heappush
a = [23,5,34,40,17]
b = [(abs(x-42),x) for x in a]
hp = []
for s in b:
    heappush(hp,s)

while hp:
    print(heappop(hp)[1])

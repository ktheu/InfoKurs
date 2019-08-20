'''
Algorithmus in 
https://en.wikipedia.org/wiki/Longest_path_problem


'''

G = {
  'a': {'b':4, 'f':12, 'g':7},
  'b': {'c':3, 'g':2},
  'c': {'d':4, 'g':4},
  'd': {},
  'e': {'d':10},
  'f': {'e':9, 'g':7},
  'g': {'d':6, 'e':11}
}

def explore(v):
    global counter
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            explore(w)
    postvisit[v] = counter
    counter += 1
    
visited = {v : False for v in G}
postvisit = {v : 0 for v in G}
counter = 1

for v in G:
    if not visited[v] :
        explore(v)

topolist = sorted(G.keys(),key=lambda v: postvisit[v],reverse = True)

inNb = {v: set() for v in G}   # dict of incoming neighbors
for v in G:
    for w in G[v]:
        inNb[w].add(v)

dist = {v: 0 for v in G}

for v in topolist:
    for w in inNb[v]:
        if dist[v] < dist[w] + G[w][v]:
            dist[v] = dist[w] + G[w][v]

print(max(dist.values()))

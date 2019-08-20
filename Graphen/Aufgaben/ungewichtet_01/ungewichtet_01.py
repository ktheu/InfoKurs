# -*- coding: utf-8 -*-

G = {
  'a': set('bcd'),
  'b': set('c'),
  'c': set('d'),
  'd': set('bc')
}

for v in G:
    print('Nachbarn von',v,':',end=' ')
    print(*sorted(G[v]))

        

# -*- coding: utf-8 -*-

G = {
'a': set('bcd'),
'b': set('ca'),
'c': set('ade'),
'd': set('ace'),
'e': set('cd')
}

for v in G:
    print('Nachbarn von',v,':',end=' ')
    print(*sorted(G[v]))

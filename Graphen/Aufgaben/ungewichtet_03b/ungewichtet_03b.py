# -*- coding: utf-8 -*-

G = {
'a': set('bcd'),
'b': set('ac'),
'c': set('abde'),
'd': set('ac'),
'e': set('c')
}

for v in G:
    print('Nachbarn von',v,':',end=' ')
    print(*sorted(G[v]))

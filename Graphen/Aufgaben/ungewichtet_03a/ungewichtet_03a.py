# -*- coding: utf-8 -*-

G = {
'a': set('bc'),
'b': set('ace'),
'c': set('abd'),
'd': set('ce'),
'e': set('bd')
}

for v in G:
    print('Nachbarn von',v,':',end=' ')
    print(*sorted(G[v]))

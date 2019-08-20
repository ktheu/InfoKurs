# -*- coding: utf-8 -*-

G = {
'a': set('bcdef'),
'b': set('ce'),
'c': set('d'),
'd': set('e'),
'e': set('f'),
'f': set('cgh'),
'g': set('fh'),
'h': set('fg')
}

for v in G:
    print('Nachbarn von',v,':',end=' ')
    print(*sorted(G[v]))
    
'''
Nachbarn von a : b c d e f
Nachbarn von b : c e
Nachbarn von c : d
Nachbarn von d : e
Nachbarn von e : f
Nachbarn von f : c g h
Nachbarn von g : f h
Nachbarn von h : f g
'''

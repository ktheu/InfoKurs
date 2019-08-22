# -*- coding: utf-8 -*-
"""
In einer list/set/dictionary der Länge 10000/100000/1000000 wird 10000 mal
ein lookup durchgeführt.
"""
import random, time

def list_lookup(n,k):
    a = [random.randint(-3*n,3*n) for i in range(n)]
    gesamtzeit = 0
    for i in range(k):
        zahl = random.randint(-3*n,3*n)
        tic = time.perf_counter()
        zahl in a   # lookup
        tac = time.perf_counter()
        gesamtzeit += (tac-tic)
    print('Zeit für {:6} lookups in einer Liste der Länge {:7}: {:9.5f} sec'.format(k,n,gesamtzeit))

def set_lookup(n,k):
    a = {random.randint(-3*n,3*n) for i in range(n)}
    gesamtzeit = 0
    for i in range(k):
        zahl = random.randint(-3*n,3*n)
        tic = time.perf_counter()
        zahl in a   # lookup
        tac = time.perf_counter()
        gesamtzeit += (tac-tic)
    print('Zeit für {:6} lookups in einem Set   der Länge {:7}: {:9.5f} sec'.format(k,n,gesamtzeit))

def dict_lookup(n,k):
    a = {random.randint(-3*n,3*n): True for i in range(n)}
    gesamtzeit = 0
    for i in range(k):
        zahl = random.randint(-3*n,3*n)
        tic = time.perf_counter()
        zahl in a   # lookup
        tac = time.perf_counter()
        gesamtzeit += (tac-tic)
    print('Zeit für {:6} lookups in einem Dict  der Länge {:7}: {:9.5f} sec'.format(k,n,gesamtzeit))
    
    
list_lookup(10000,10000)
list_lookup(100000,10000)
list_lookup(1000000,10000)
set_lookup(10000,10000)
set_lookup(100000,10000)
set_lookup(1000000,10000)
dict_lookup(10000,10000)
dict_lookup(100000,10000)
dict_lookup(1000000,10000)
    
'''
Zeit für  10000 lookups in einer Liste der Länge   10000:   1.41452 sec
Zeit für  10000 lookups in einer Liste der Länge  100000:  14.11062 sec
Zeit für  10000 lookups in einer Liste der Länge 1000000: 151.81383 sec
Zeit für  10000 lookups in einem Set   der Länge   10000:   0.00134 sec
Zeit für  10000 lookups in einem Set   der Länge  100000:   0.00209 sec
Zeit für  10000 lookups in einem Set   der Länge 1000000:   0.00245 sec
Zeit für  10000 lookups in einem Dict  der Länge   10000:   0.00178 sec
Zeit für  10000 lookups in einem Dict  der Länge  100000:   0.00174 sec
Zeit für  10000 lookups in einem Dict  der Länge 1000000:   0.00274 sec
'''  

 
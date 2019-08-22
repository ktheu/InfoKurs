# -*- coding: utf-8 -*-
"""
Heap vs. Liste
In einen Heap/Liste der Länge 1000/10000/100000 werden 1000 Runden durchgeführt.
Eine Runde besteht darin, dass 100 zufällige Zahlen eingefügt werden und
anschließend die niedrigsten 100 wieder entfernt werden.
"""
import random, time
from heapq import heapify, heappop, heappush

def heap_runden(n,k):
    a = [random.randint(-3*n,3*n) for i in range(n)]
    heapify(a) 
    
    tic = time.perf_counter()
    for i in range(k):
        for i in range(100):
            heappush(a,random.randint(-3*n,3*n))
        for i in range(100):
            mini = heappop(a)
    tac = time.perf_counter()
    gesamtzeit = tac-tic
    print('Zeit für {:6} Runden in einem Heap  der Länge {:7}: {:9.5f} sec'.format(k,n,gesamtzeit))

def list_runden(n,k):
    a = [random.randint(-3*n,3*n) for i in range(n)]
   
    tic = time.perf_counter()
    for i in range(k):
        for i in range(100):
            a.append(random.randint(-3*n,3*n))
        a.sort(reverse=True)
        for i in range(100):
            a.pop()
    tac = time.perf_counter()
    gesamtzeit = tac-tic
    print('Zeit für {:6} Runden in einer Liste der Länge {:7}: {:9.5f} sec'.format(k,n,gesamtzeit))

heap_runden(10000,1000)
heap_runden(100000,1000)
heap_runden(1000000,1000)
list_runden(10000,1000)
list_runden(100000,1000)
list_runden(1000000,1000)
    
'''
Zeit für   1000 Runden in einem Heap  der Länge   10000:   0.16732 sec
Zeit für   1000 Runden in einem Heap  der Länge  100000:   0.18933 sec
Zeit für   1000 Runden in einem Heap  der Länge 1000000:   0.25440 sec
Zeit für   1000 Runden in einer Liste der Länge   10000:   0.32491 sec
Zeit für   1000 Runden in einer Liste der Länge  100000:   1.95415 sec
Zeit für   1000 Runden in einer Liste der Länge 1000000:  62.84779 sec
'''  

 
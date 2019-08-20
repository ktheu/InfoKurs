# -*- coding: utf-8 -*-
"""
"""

def f(x):
    return x % 10

def insert(ht,x): 
    hwert = f(x)
    step = 0
    while ht[hwert] is not None:
        step +=1
        hwert = (f(x) + (step*step)) % 10
    ht[hwert] = x

def insertfolge(ht,a):
    for x in a:
        insert(ht,x)
    return tuple(ht.values())

tup = (36, 20, 62, 22, None, None, 42, 37, 12, None)

import itertools

a = [62,22,42,37,36,20,12]
aperm = list(itertools.permutations(a, 7))
print(len(aperm))

for tip in aperm:
    ht = {k:None for k in range(10)}

    v = insertfolge(ht,tip)
    if v == tup: print(*tip)





        
        


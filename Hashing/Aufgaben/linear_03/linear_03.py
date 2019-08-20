# -*- coding: utf-8 -*-
"""
"""

a = [27,17,16,26,8,35,29]

def printfolge(a):
    a = list(a)
    for i in range(len(a)):
        if a[i] is None: a[i] = '.'
        print('{:>4}'.format(a[i]),end='')
    print()

def f(x):
    return x % 10

def insert(ht,x):
    hwert = f(x)
    step = 0
    while ht[hwert] is not None:
        step +=1
        hwert = (f(x) + (step)) % 10   # lineares Sondieren
    ht[hwert] = x

def insertfolge(ht,a):
    for x in a:
        insert(ht,x)
    return tuple(ht.values())

ht = {k:None for k in range(10)}
insertfolge(ht,a)
print("Zahlenfolge:")
print(*a)
print()
printfolge(ht.keys())
printfolge(ht.values())

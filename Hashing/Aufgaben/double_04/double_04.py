# -*- coding: utf-8 -*-
a = [27,8,18,16,57,48,37]

def printfolge(a):
    a = list(a)
    for i in range(len(a)):
        if a[i] is None: a[i] = '.'
        print('{:>4}'.format(a[i]),end='')
    print()

def f(x):
    return x % 10

def f2(x):
    return (2*x+7)%10

def insert(ht,x):
    hwert = f(x)
    step = 0
    while ht[hwert] is not None:
        step +=1
        hwert = (f(x) + (step*f2(x))) % 10   # quadratisches Sondieren
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

#tup = (36, 20, 62, 22, None, None, 42, 37, 12, None)
#
#import itertools

#a = [62,22,42,37,36,20,12]
#aperm = list(itertools.permutations(a, 7))
#print(len(aperm))
#
#for tip in aperm:
#    ht = {k:None for k in range(10)}
#
#    v = insertfolge(ht,tip)
#    if v == tup: print(*tip)

# -*- coding: utf-8 -*-
def floyd (c):
    n = len(c)
    d = [[0]*n for j in range(n)]
    p = [[0]*n for j in range(n)]
    for i in range(n):
        for j in range(n):
            d[i][j] = c[i][j]
            p[i][j] = i

    print('Ausgangsmatrix: ')
    printMatrix(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                tmp = d[i][k] + d[k][j]
                if tmp < d[i][j]:
                    d[i][j] = tmp
                    p[i][j] = p[k][j]
        print('Matrix k =',k)
        printMatrix(d)
    return d, p

def printPath(p, i, j):
    if i== j: print(chr(i+97),end='')
    else:
        printPath(p,i,p[i][j])
        print(' - ' + chr(j+97),end='')

def printMatrix(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == inf:
                print("{:4s}".format("."),end='')
            else:
                print("{:<4.0f}".format(a[i][j]),end='')
        print()

def printNachbarn():
    n = len(G)
    for x in range(n):
        nb = [chr(y+97) for y in range(n) if x != y and G[x][y]  < inf ]
        print('Nachbarn von',chr(x+97),end=': ')
        for w in nb:
            print(w,G[x][ord(w)-97],end=' ')
        print()


inf = float('inf')
G = [[0, 4, 1, inf, inf],
 [3, 0, 1, inf,2],
 [1, 3, 0, inf, inf],
 [inf, 2, 5, 0, inf],
 [inf, 7, inf, 3, 0],
 ]

printNachbarn()

d, p = floyd(G)
von = 'a'
bis = 'e'

vi, wi = ord(von)-97, ord(bis)-97
print("\nKürzester Weg von",von,"nach",bis)
printPath(p, vi , wi)
print()
print("Kosten =",d[vi][wi])

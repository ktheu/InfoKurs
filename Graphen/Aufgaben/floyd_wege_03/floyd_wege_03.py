# -*- coding: utf-8 -*-
def floyd (c):
    n = len(c)
    d = [[0]*n for j in range(n)]
    p = [[0]*n for j in range(n)]
    for i in range(n):
        for j in range(n):
            d[i][j] = c[i][j]
            p[i][j] = i

    printMatrix(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                tmp = d[i][k] + d[k][j]
                if tmp < d[i][j]:
                    d[i][j] = tmp
                    p[i][j] = p[k][j]
    return d, p

def printPath(p, i, j):
    if i== j: print(chr(i+97),end='')
    else:
        printPath(p,i,p[i][j])
        print(' - ' + chr(j+97) + ' (' + str(G[p[i][j]][j]) + ') ',end='')

def printMatrix(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == inf:
                print("{:4s}".format("."),end='')
            else:
                print("{:<4.0f}".format(a[i][j]),end='')
        print()

def weg(v,w):



    d, p = floyd(G)
    print('Berechnete Kostenmatrix:')
    printMatrix(d)
    print('Berechnete Wegematrix:')
    printMatrix(p)


    vi, wi = ord(v)-97, ord(w)-97
    print("\nKürzester Weg von",v,"nach",w)
    print("(Kosten der Teilstrecken in Klammern)")
    printPath(p, vi , wi)
    print()
    print("Gesamtkosten =",d[vi][wi])

inf = float('inf')
G = [[0, 2, 2, 6, inf],
 [1, 0, 4, inf,13],
 [11, inf, 0, 1, 5],
 [inf, inf, inf, 0, 1],
 [inf, inf, inf, inf, 0],
 ]

for x in range(len(G)):
    nb = [chr(y+97) for y in range(len(G)) if x != y and G[x][y]  < inf ]
    print('Nachbarn von',chr(x+97),end=': ')
    for w in nb:
        print(w,G[x][ord(w)-97],end=' ')
    print()

weg('b','e')

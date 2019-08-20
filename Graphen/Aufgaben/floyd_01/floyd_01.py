# -*- coding: utf-8 -*-
'''
Die Knoten heißen a,b,c,d ... und
haben die Matrixnummern 0,1,2,3 ...
'''
def floyd (c):
    n = len(c)
    d = [[0]*n for j in range(n)]
    p = [[0]*n for j in range(n)]    
    for i in range(n):
        for j in range(n):
            d[i][j] = c[i][j]
            p[i][j] = i
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                tmp = d[i][k] + d[k][j]
                if tmp < d[i][j]:
                    d[i][j] = tmp
                    p[i][j] = p[k][j]
    return d, p

#def getPath(p, i, j):
#    if i == j: return chr(i+97)
#    return getPath(p,i,p[i][j]) + ' - ' + chr(j+97)

def getPath(p, i, j):
    if i == j: return str(i)
    return getPath(p,i,p[i][j]) + ' - ' + str(j)

def printMatrix(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == inf:
                print("{:4}".format("."),end='')
            else:
                print("{:<4}".format(a[i][j]),end='')
        print()
    print()
        
inf = float('inf')
G = [[0,   8,   2, inf],  
     [inf, 0, inf,   4],  
     [inf, 1,   0,   6],  
     [inf, 2, inf,   0]]  
        
d, p = floyd(G)

print("Gegebenen Kostenmatrix:")
printMatrix(G)

print("Errechnete Distanzmatrix:")
printMatrix(d)

print("Errechnete Wegematrix:")
printMatrix(p)

v, w = 'a','b'     # Start und Zielknoten
vi, wi = ord(v)-97, ord(w)-97
print("Kürzester Weg von",v,"nach",w)
print(getPath(p,vi,wi))
print("Kosten =",d[vi][wi])
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 20:26:41 2018

@author: khthe
"""

'''
Lies den Text bis 1.1 einschließlich. Implementiere dann
die im Text beschriebene Adjazenzmatrix G als eine Liste von Listen
2 = Don't care
'''
G = [[1,1,2,2,2],
     [0,1,2,2,2],
     [2,2,1,0,1],
     [2,2,0,1,1],
     [2,2,2,2,1]]

'''
Implementiere die Funktion pruefe_symmetrie<_spezialfall(G)
'''
def pruefe_symmetrie_spezialfall(G):
    n = len(G)
    for i in range(n):
        for j in range(i,n):
            if G[i][j] != G[j][i]:
                return False
    return True

#print(pruefe_symmetrie_spezialfall(G))
'''
Gib ein Beispiel für eine Matrix, die die symmetrie
Prüfung besteht, und für die sich doch keine zulässige
Belegung finden lässt.

Beispiel (wie im Text angedeutet): Die Matrix für 
Danni, Lotta und Steffi 
'''
def fuelle_zimmer(s,G):
    Z = set()
    Q = {s}
    while Q:
        i = Q.pop()
        Z.add(i)
        for j in range(len(G)):
            if G[i][j] == 1 and j not in Q | Z:
                Q.add(j)
    return Z


def pruefe_zimmer(Z,G):
    for i in Z:
        for j in Z:
            if i !=j and G[i][j] == 0:
                return False
    return True

def erstelle_belegung(G):
    B = []
    L = {k for k in range(len(G))}
    while L:
        s = L.pop()
        Z = fuelle_zimmer(s,G)
        if not pruefe_zimmer(Z,G):
            return False
        B.append(L)
    end
    return B

def pruefe_symmetrie_allgemein(G):
    n = len(G)
    for i in range(n):
        for j in range(i,n):
            if G[i][j] != G[j][i] and G[i][j] != 2 and G[j][i] != 2:
                return False
    return True

def eliminiere_dont_cares(G):
    N = len(G)
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1 and G[j][i] == 2:
                G[j][i] = 1
            elif G[i][j] == 0 and G[j][i] == 2:
                G[j][i] = 0
    return G

def readdata(nr):
    '''
    nr - int
    returns: zwei dictionaries, die mit den namen als keys und
    den mengen der vorlieben bzw. abneigungen als set,
    gelesen von den datensätzen in zimmerbelegung<nr>.txt
    '''
    datapath = 'C:/Users/khthe/Dropbox/Informatik/Bwinf/b36_a1_zimmerbelegung/aufgabenstellung/material/'
    with open(datapath+'zimmerbelegung'+str(nr)+'.txt',encoding='utf8') as f:
       zeilen = f.read().splitlines()
       
    plus = {}
    minus = {}
    for s in zeilen:
        s = s.strip()
        if len(s) == 0: continue
        if s[0] not in '+- ':
            name = s
        if s[0] == '+':
            addmap(plus,name,s[1:])
        if s[0] == '-':
            addmap(minus,name,s[1:])
    return plus, minus

def addmap(m,name,s):
    '''
    m: dictionary
    name, s: String
    returns: nichts, fuegt in das dictionary m einen Eintrag
       m[name] = set(Teilstring1, Teilstring2 ... )
       wobei die Teilstrings die mit blank getrennten Teile von s sind.
    '''
    tmp = set()
    for s0 in s.split():
        tmp.add(s0.strip())
    m[name] = tmp
    

plus,minus = readdata(1)
print(plus)
print(minus)
    
    


    

        


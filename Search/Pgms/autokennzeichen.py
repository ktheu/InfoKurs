# -*- coding: utf-8 -*-
"""
status = (wort, nr)
wort: String, der noch zu verteilenden Buchstaben
nr: 0 / 1 - Position, die bei der nächsten Verteilung dran ist
    0 = als nächstes ist die vordere Position dran (kuerzelliste)
    1 = als nächstes ist die mittlere Position dran (1 oder 2 Buchstaben)
    
endstatus = ('', 0)
    es ist nichts mehr zu verteilen und als nächstes wäre die
    vordere Position dran

Eingaben:
    
BIBER
BUNDESWETTBEWERB
CLINTON
DONAUDAMPFSCHIFFFAHRTSKAPITÄNSMÜTZE
ETHERNET
INFORMATIK
LLANFAIRPWLLGWYNGYLLGOGERYCHWYRNDROBWLLLLANTYSILIOGOGOGOCH
RINDFLEISCHETIKETTIERUNGSÜBERWACHUNGSAUFGABENÜBERTRAGUNGSGESETZ
SOFTWARE
TRUMP
TSCHÜSS
VERKEHRSWEGEPLANUNGSBESCHLEUNIGUNGSGESETZ
"""
from heapq import heappop, heappush
from collections import deque
import time


    
def readdata():
    with open('kuerzelliste.txt') as f:
        kuerzel = f.read().splitlines() 
    return kuerzel

def reconstructPath(prev):
    s = ('',0)
    a = []
    while prev[s] is not None:
        print(s)
        w,_ = prev[s]
        a.append(w)
        s = prev[s]
    print(s)
    a.reverse()
    tmp = []
    for i in range(len(a)-1):
        tmp.append(a[i][:-len(a[i+1])])
    tmp.append(a[-1])
    
    knr = 101   # kennzeichennummer
    for i in range(0,len(tmp),2):
        print(tmp[i]+'-'+tmp[i+1]+'-'+str(knr))
        knr+=1
   

def goaltest(state):
    wort, nr = state
    return wort == '' and nr == 0
    
def nextstates(state):
    wort, nr = state
    tmp = []
    if nr == 0:
        for k in kuerzel:
            if wort.startswith(k):
                if len(wort[len(k):]) > 0:
                    tmp.append((wort[len(k):],1))
    else:
        tmp.append((wort[1:],0))
        tmp.append((wort[2:],0))
    return tmp     

def bfs(s):
    frontier =  deque([s])
    prev = {s:None}
    nrExplored = 0
    while frontier:
        state = frontier.popleft()  
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state
    return None,nrExplored

def dfs(s):
    frontier =  [s]
    prev = {s:None}
    nrExplored = 0
    while frontier:
        state = frontier.pop()  
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        nxt = nextstates(state)
        nxt.reverse()
        for v in nxt:
            if v not in prev:
                frontier.append(v)
                
                prev[v] = state
    return None,nrExplored

def h(s):
    return len(s[0])

def greedy(s):
    frontier =[(h(s),s)]  
    prev = {s:None}
    nrExplored = 0
    while frontier:
        _ ,state = heappop(frontier)  
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        for v in nextstates(state):
            if v not in prev:
                heappush(frontier,(h(v),v))
                prev[v] = state

def astar(s):
    frontier =[(h(s),s)]  
    prev = {s:None}
    nrExplored = 0
    g = {s:0}  # backword costs: hier die Anzahl Züge
    while frontier:
        _ ,state = heappop(frontier)  # die Kosten braucht man an der Stelle nicht
        nrExplored+=1
        if goaltest(state):
            return prev,nrExplored
        for v in nextstates(state):
            if v not in prev:
                g[v] = g[state]+1
                heappush(frontier,(g[v]+h(v),v))
                prev[v] = state

kuerzel = readdata()
startstate = ('LLANFAIRPWLLGWYNGYLLGOGERYCHWYRNDROBWLLLLANTYSILIOGOGOGOCH',0)
start = time.perf_counter()
prev,nrExplored = bfs(startstate) 
laufzeit = time.perf_counter()-start
print(laufzeit, nrExplored)
if prev is None:
    print('keine Lösung')
else:
    reconstructPath(prev)



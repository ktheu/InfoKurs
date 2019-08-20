'''
Ein state ist ein Tupel (x,y) in einem grid (einer
Liste mit Listen von Tupeln)
'''
def showGrid():
    for a in grid:
        print(''.join(a))

def getStartAndGoal():
    '''
    returns: Tuple (startstate, goalstate)
    '''
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'S':
                startstate = (x,y)
            elif grid[x][y] == 'E':
                goalstate = (x,y)
    return startstate, goalstate

def goaltest(state):
    return grid[state[0]][state[1]]  == 'E'

def free(state):
    return grid[state[0]][state[1]] != 'x'

def nextstates(state):
    '''
    returns: Liste mit angrenzenden freien Tupeln.
    '''
    tmp = []
    x, y = state
    links, rechts, oben, unten = (x,y-1), (x,y+1), (x-1,y), (x+1,y)
    linksfrei = (y > 0 and free(links))
    rechtsfrei = (y < spalten and free(rechts))
    obenfrei = (x > 0 and free(oben))
    untenfrei = (x < zeilen and free(unten))
    if obenfrei: tmp.append(oben)
    if untenfrei: tmp.append(unten)
    if linksfrei: tmp.append(links)
    if rechtsfrei: tmp.append(rechts)
    return tmp

def reconstructPath(prev,state):
    s = state
    tmp = []
    while prev[s] is not None:
        tmp.append(s)
        s = prev[s]
    tmp.reverse()
    return tmp,len(tmp)

def showResult():
    '''
    gefundener Weg: 'o', explored: '.', frontier: '~'
    '''
    for state in path[:-1]:
        x, y = state
        grid[x][y] = 'o'

    for state in explored:
        x, y = state
        if grid[x][y] == ' ':
            grid[x][y] = '.'

    '''
    for state in prev:
        x, y = state
        if grid[x][y] not in 'o.SE':
            grid[x][y] = '~'
    '''
    showGrid()
    print("explored = {}, weglänge = {}".format(len(explored), weglaenge))

from collections import deque
def bfs(s):
    frontier =  deque([s])
    prev = {s:None}
    explored = set()

    while frontier:
        state = frontier.popleft()
        explored.add(state)
        if goaltest(state):
            return prev, explored
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state

def dfs(s):
    frontier =  [s]
    prev = {s:None}
    explored = set()

    while frontier:
        state = frontier.pop()
        explored.add(state)
        if goaltest(state):
            return prev,explored
        nxt = nextstates(state)
        nxt.reverse()        # die linken Kinder sollen zuletzt auf den frontier-Keller
        for v in nxt:
            if v not in prev:
                frontier.append(v)
                prev[v] = state

def h(state):
    ''' Euklidsche-Distanz '''
    x1, y1 = state
    x2, y2 = goalstate
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def h2(state):
    ''' Manhatten-Distanz '''
    x1, y1 = state
    x2, y2 = goalstate
    return abs(x1-x2) + abs(y1-y2)

from heapq import heappop, heappush
def greedy(s):
    frontier =[(h(s),s)]
    prev = {s:None}
    explored = set()
    while frontier:
        _ ,state = heappop(frontier)
        explored.add(state)
        if goaltest(state):
            return prev,explored
        for v in nextstates(state):
            if v not in prev:
                heappush(frontier,(h(v),v))
                prev[v] = state

def astar(s):
    frontier =[(h(s),s)]
    prev = {s:None}
    explored = set()
    g = {s:0}                         # backword costs
    while frontier:
        _ ,state = heappop(frontier)  # die Kosten braucht man an der Stelle nicht
        explored.add(state)
        if goaltest(state):
            return prev,explored
        for v in nextstates(state):
            if v not in prev:
                g[v] = g[state]+1
                if v == (2,6) or v == (4,7):
                    print(v,g[v]+h2(v))
                heappush(frontier,(g[v]+h2(v),v))
                prev[v] = state

with open ("maze_01.txt") as f:
    lines = f.read().splitlines()

grid = [list(s) for s in lines if len(s)>0]
zeilen, spalten = len(grid), len(grid[0])
startstate, goalstate = getStartAndGoal()

prev, explored = astar(startstate)     # bfs, dfs, greedy, astar
path, weglaenge = reconstructPath(prev,goalstate)

showResult()

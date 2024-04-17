Die Tiefensuche ist nicht geeignet, um den kürzesten Weg zu finden.

```
def dfs(s):
    frontier =  [startstate]
    prev = {startstate:None}
    while frontier:
        state = frontier.pop()  
        if goaltest(state):
            return prev,state
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state
    return None, None
```

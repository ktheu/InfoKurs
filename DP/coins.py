def dp(i):
    '''
    returns: die minimale Anzahl von Münzen, um in der Summe x zu erreichen
    dp-guess: welches ist die erste Münze der optimalen Lösung?
    '''
    if i in memo: return memo[i]
    if i == 0: return 0                           # Für die Summe 0 gibt es eine Lösung: keine Münzen
        
    res = float('inf')                            # noch keine Lösung gefunden
    for c in coins:
        if i-c >= 0 and 1 + dp(i-c) < res:
            res = 1 + dp(i-c)
    memo[i] = res
    return res

n, x = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]
memo = {}
print(dp(x))
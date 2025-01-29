def trib(k):
    if k == 0:
        return 0
    if k == 1 or k == 2:
        return 1
    if k not in memo:
        memo[k] = trib(k-3)+trib(k-2)+trib(k-1)
    return memo[k]


memo = {}
print(trib(6))

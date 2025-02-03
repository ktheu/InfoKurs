def dp(i, k):
    if i >= n:
        return 0
    if (i,k) in memo: return memo[(i,k)]
    if k == 0:
        res = max(dp(i+1,1),dp(i+1,2)) - a[i]
    elif k == 1:
        res = a[i] + dp(i+1,2)
    elif k == 2:
        res = max(dp(i+1,0),dp(i+1,2))
    memo[(i,k)] = res
    return res


# a = [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48,
#           52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11, 94]
# a = [1,2,3,0,2]
memo = dict()
a = [1,2,4]
n = len(a)
dp(2,2)
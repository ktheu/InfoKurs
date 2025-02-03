'''
0 - keine Aktie vorhanden, nicht in cooldown
1 - keine Aktie n, in cooldown
2 - Aktie vorhanden
'''

def dp(i, k):
    if i == n-1:
        if k == 0 or k == 1:
            prev[(i,k)] = None
            return 0
        else:
            prev[(i,k)] = None
            return a[i]
    if (i,k) in memo: return memo[(i,k)]
    if k == 0:
        res = dp(i+1,0)
        prev[(i,k)] = (i+1,0)
        if dp(i+1,2) - a[i] > res:
            res = dp(i+1,2) - a[i]
            prev[(i,k)] = (i+1,2)

    
    elif k == 1:
        res = dp(i+1,0)
        prev[(i,k)] = (i+1,0)
    elif k == 2:
        res = dp(i+1,2)
        prev[(i,k)] = (i+1,2)
        if dp(i+1,1) + a[i] > res:
            res =  dp(i+1,1) + a[i] 
            prev[(i,k)] = (i+1,1)
            
       
    memo[(i,k)] = res
    return res

prev = dict()
memo = dict()
a = [1,2,3,0,2]
n = len(a)
dp(0,0)
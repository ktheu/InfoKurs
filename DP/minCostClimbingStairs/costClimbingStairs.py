'''
You are given an integer array cost where cost[i] 
is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

'''
stairs(k) = minimum cost to reach index k

'''

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#cost = [10, 15, 20]


def stairs(k):
    if k == 0 or k == 1:
        return 0
    return min(stairs(k-2)+cost[k-2], stairs(k-1)+cost[k-1])


n = len(cost)
print(stairs(n))

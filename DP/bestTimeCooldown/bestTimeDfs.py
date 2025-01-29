from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs():
            startstate = (-1, 'Hn', 0)
            best = 0
            frontier = [startstate]
            prev = {startstate: None}
            nrExplored = 0
            while frontier:
                state = frontier.pop()
                _, _, profit = state
                if profit > best:
                    best = profit
                nrExplored += 1
                for v in nextstates(state):
                    if v not in prev:
                        frontier.append(v)
            return best

        def nextstates(state):
            tmp = []
            i, mode, profit = state
            if i+1 < len(prices):
                if mode == 'H':
                    tmp.append((i+2, 'Hn', profit+prices[i+1]))
                    tmp.append((i+1, 'H', profit))
                if mode == 'Hn':
                    tmp.append((i+1, 'H', profit-prices[i+1]))
                    tmp.append((i+1, 'Hn', profit))
            return tmp

        return dfs()


prices = [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48,
          52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11, 94]

s = Solution()
print(s.maxProfit(prices))

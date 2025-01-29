from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def g(i, h):
            if i >= len(prices):
                return 0
            if not h:
                return max(g(i+1, False), g(i+1, True)-prices[i])
            else:
                return max(g(i+1, True), g(i+2, False)+prices[i])

        return g(0, False)


s = Solution()
prices = [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48,
          52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11, 94]
print(s.maxProfit(prices))
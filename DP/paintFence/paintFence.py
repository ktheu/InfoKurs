from typing import List
from functools import lru_cache


class Solution:
    def numWays(self, n: int, k: int) -> int:

        @lru_cache(None)
        def g(i, h):
            if i >= n:
                return k
            if not h:
                return (k-1)*g(i+1, False) + g(i+1, True)
            else:
                return (k-1)*g(i+1, False)

        return g(1, False)


s = Solution()

print(s.numWays(2, 1))

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        inf = float('inf')
        H, Hn, Hnc = -prices[0], 0, -inf
        for i in range(1, len(prices)):
            H, Hn, Hnc = max(H, Hn-prices[i]), max(Hn, Hnc), H+prices[i]
        return max(H, Hn, Hnc)


s = Solution()
prices = [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48,
          52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11, 94]
print(s.maxProfit(prices))

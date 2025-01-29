class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[int(s) for s in row] for row in matrix]
        for r in range(1, m):
            for c in range(1, n):
                if dp[r][c]:
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1]) + 1

        max_len = 0
        for r in range(m):
            for c in range(n):
                max_len = max(max_len, dp[r][c])
        return max_len*max_len

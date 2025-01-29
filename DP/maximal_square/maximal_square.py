class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def dp(i, j):
            '''
            area of the largest square with bottom-right index i, j.
            '''
            if matrix[i][j] == "0":
                return 0
            if i == 0 or j == 0:
                return 0 if matrix[i][j] == "0" else 1
            if (i, j) not in memo:
                if matrix[i][j] == 0:
                    memo[(i, j)] = 0
                else:
                    left = dp(i, j-1)
                    up = dp(i-1, j)
                    leftup = dp(i-1, j-1)
                    k = min(left, up, leftup)
                    if k == 0:
                        memo[(i, j)] = 1
                    else:
                        memo[(i, j)] = (k+1)

            return memo[(i, j)]

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                dp(i, j)
        dp(m-1, n-1)
        a = max([dp(i, j) for i in range(m) for j in range(n)])
        return a**2

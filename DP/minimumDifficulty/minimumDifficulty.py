from typing import List


class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)
        if n < d:
            return -1
        tab = [[0]*n for _ in range(d)]
        for y in range(1, n):
            tab[0][y] = '-'
        for x in range(1, d):
            for y in range(n-d+1+x, n):
                tab[x][y] = '-'
            for y in range(x):
                tab[x][y] = '-'
        maxdiff = 0
        for y in range(n-1, d-2, -1):
            maxdiff = max(maxdiff, jobDifficulty[y])
            tab[d-1][y] = maxdiff
        for x in range(d-2, -1, -1):
            for y in range(n-1):
                if tab[x][y] != '-':
                    hardest = jobDifficulty[y]
                    best = hardest+tab[x+1][y+1]
                    for k in range(y+1, n-1):
                        if tab[x+1][k+1] != '-':
                            hardest = max(hardest, jobDifficulty[k])

                            best = min(best, hardest+tab[x+1][k+1])
                    tab[x][y] = best

        return tab[0][0]


s = Solution()
print(s.minDifficulty([1, 1, 1], 3))

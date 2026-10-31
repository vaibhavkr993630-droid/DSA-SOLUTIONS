class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if right[i][j] and i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + right[i][j]) % MOD

                    if down[i][j] and j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + down[i][j]) % MOD

                else:
                    ways = (dp[i][j] + right[i][j] + down[i][j]) % MOD

                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + ways) % MOD

                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + ways) % MOD

        return (dp[m-1][n-1] + right[m-1][n-1] + down[m-1][n-1]) % MOD
import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[x][y] 到达坐标x,y 可选的路径条数
        dp = np.zeros((m, n))
        for i in range(m): dp[i][0] = 1
        for j in range(n): dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return int(dp[m-1][n-1])
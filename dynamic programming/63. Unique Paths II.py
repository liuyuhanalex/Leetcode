from typing import List
import numpy as np

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        dp = np.zeros((len(obstacleGrid), len(obstacleGrid[0])))
        dp[0][0] = 1
        for i in range(1, len(obstacleGrid)):
            dp[i][0] = 1 if obstacleGrid[i][0] != 1 and dp[i-1][0] != 0 else 0
        for j in range(1, len(obstacleGrid[0])): dp[0][j] = 1 if obstacleGrid[0][j] != 1 and dp[0][j-1] != 0 else 0
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] != 1 else 0
        return int(dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1])
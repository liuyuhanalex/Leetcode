from typing import List
import numpy as np


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = np.zeros((len(grid), len(grid[0])))
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid[0])): dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, len(grid)): dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return int(dp[len(grid) - 1][len(grid[0]) - 1])


if __name__ == '__main__':
    print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(Solution().minPathSum([[1]]))

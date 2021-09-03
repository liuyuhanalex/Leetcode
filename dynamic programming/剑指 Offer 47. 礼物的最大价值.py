from typing import List
import numpy as np


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = np.zeros((len(grid), len(grid[0])))
        another_dp = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                point = (i-1, j) if dp[i-1][j] > dp[i][j-1] else (i, j-1)
                another_dp[(i, j)] = point
        start_point = (len(grid)-1, len(grid[0])-1)
        path = [grid[start_point[0]][start_point[1]]]
        while start_point != (0, 0):
            point = another_dp.get(start_point)
            start_point = point
            path.append(grid[point[0]][point[1]])
        print('->'.join([str(i) for i in reversed(path)]))
        return dp[len(grid)-1][len(grid[0])-1]
    
    
if __name__ == '__main__':
    Solution().maxValue([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]])

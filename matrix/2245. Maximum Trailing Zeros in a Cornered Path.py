from typing import List
from copy import deepcopy

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        prefix_grid_x = deepcopy(grid)
        prefix_grid_y = deepcopy(grid)
        for i in range(len(grid)):
            for j in range(1, len(grid[0])):
                prefix_grid_x[i][j] *= prefix_grid_x[i][j-1]
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                prefix_grid_y[i][j] *= prefix_grid_y[i-1][j]
        final_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        print(final_grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                pass




if __name__ == '__main__':
    Solution().maxTrailingZeros(grid = [[4,3,2],[7,6,1],[8,8,8]])

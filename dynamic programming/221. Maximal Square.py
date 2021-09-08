from typing import List
import numpy as np


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        w = len(matrix[0])
        dp = [[0 for _ in range(w)] for _ in range(h)]
        max_num = 0
        for i in range(0, h):
            for j in range(0, w):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    if dp[i][j] > max_num:
                        max_num = dp[i][j]
        return max_num*max_num


if __name__ == '__main__':
    print(Solution().maximalSquare([["1","0","1","0","0"],
                                    ["1","0","1","1","1"],
                                    ["1","1","1","1","1"],
                                    ["1","0","0","1","0"]]))
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        w = len(matrix[0])
        dp = [[[0,0] for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == '1':
                    dp[i][j] = [1, 1]
        for i in range(1, h):
            for j in range(0, w):
                if matrix[i][j] == '1':
                    w_1 = min(dp[i-1][j][0], dp[i][j-1][0], 1)
                    h_1 = max(dp[i-1][j][1], dp[i][j-1][1], 1)
                    print(i, j, w_1, h_1)
                    if w_1 == 1:
                        h_1 += 1
                    if h_1 == 1:
                        w_1 += 1
                    dp[i][j] = [w_1, h_1]
        print(dp)


if __name__ == '__main__':
    Solution().maximalRectangle([["1","0","1","0","0"],
                                 ["1","0","1","1","1"],
                                 ["1","1","1","1","1"],
                                 ["1","0","0","1","0"]])
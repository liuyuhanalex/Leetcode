from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp[0] = matrix[0]
        r, c = len(matrix)-1, len(matrix[0]) - 1
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                res = dp[i-1][j]
                if j+1 <= c and dp[i-1][j+1]<res:
                    res = dp[i-1][j+1]
                if j-1 >= 0 and dp[i-1][j-1]<res:
                    res = dp[i-1][j-1]
                dp[i][j] = res + matrix[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    print(Solution().minFallingPathSum(matrix=[[2, 1, 3],
                                               [6, 5, 4],
                                               [7, 8, 9]]))

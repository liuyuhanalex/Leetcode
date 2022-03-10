from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1 for _ in range(i+1)] for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[-1]



if __name__ == '__main__':
    Solution().getRow(rowIndex = 3)
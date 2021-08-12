import numpy as np

class Solution:
    def integerBreak(self, n: int) -> int:
        # dp 的含义，分拆数字i可以得到的最大乘积 dp[i]
        dp = [i-1 for i in range(n+1)]
        dp[0] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i-j)*j, dp[i-j]*j))
        return dp[-1]

if __name__ == '__main__':
    print(Solution().integerBreak(2))
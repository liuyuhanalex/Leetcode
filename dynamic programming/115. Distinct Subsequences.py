import numpy as np


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]的含义为在s[0:i]中找到t[0:j]的方案数
        dp = np.zeros((len(s), len(t)))
        for i in range(0, len(s)):
            if s[i] == t[0]:
                dp[i][0] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0]
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)-1][len(t)-1]


if __name__ == '__main__':
    print(Solution().numDistinct(s="rabbbit", t="rabbit"))
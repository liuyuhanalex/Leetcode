class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # dp[i], 第i位以1或者0结尾的最小flip次数
        dp = [[0, 0] for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == '1':
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])
            else:
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
                dp[i][0] = dp[i-1][0]
        return min(dp[-1])


if __name__ == '__main__':
    Solution().minFlipsMonoIncr(s = "00011000")
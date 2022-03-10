class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] + ord(s1[i - 1])
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s2[i - 1])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[j - 1] == s2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(ord(s1[j - 1]) + dp[i][j - 1], ord(s2[i - 1]) + dp[i - 1][j])
        return dp[-1][-1]




if __name__ == '__main__':
    print(Solution().minimumDeleteSum(s1 = "delete", s2 = "leet"))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1))] for _ in range(len(word2))]
        for i in range(len(word1)):
            if word1[i] == word2[0]:
                dp[0][i] = 1
            if dp[0][i - 1] == 1:
                dp[0][i] = 1
        for i in range(len(word2)):
            if word1[0] == word2[i]:
                dp[i][0] = 1
            if dp[i - 1][0] == 1:
                dp[i][0] = 1
        for i in range(1, len(word2)):
            for j in range(1, len(word1)):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - dp[len(word2) - 1][len(word1) - 1] * 2


if __name__ == '__main__':
    Solution().minDistance()
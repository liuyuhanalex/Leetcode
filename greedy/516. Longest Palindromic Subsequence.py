class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] 的意义为区间i到j之间最长的回文串长度
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][len(s)-1]



if __name__ == '__main__':
    Solution().longestPalindromeSubseq("bbbab")
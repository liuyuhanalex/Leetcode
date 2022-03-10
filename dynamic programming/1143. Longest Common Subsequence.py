class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                dp[0][i] = 1
            if dp[0][i-1] == 1:
                dp[0][i] = 1
        for i in range(len(text2)):
            if text1[0] == text2[i]:
                dp[i][0] = 1
            if dp[i-1][0] == 1:
                dp[i][0] = 1
        for i in range(1, len(text2)):
            for j in range(1, len(text1)):
                if text1[j] == text2[i]:
                    print('i:{}, j:{}, dp[i-1][j-1]:{}'.format(i, j, dp[i-1][j-1]))
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text2)-1][len(text1)-1]




if __name__ == '__main__':
    print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
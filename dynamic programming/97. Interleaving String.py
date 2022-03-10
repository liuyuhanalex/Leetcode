class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == '':
            return s2==s3
        if s2 == '':
            return s1==s3
        dp = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            dp[0][i] = True if s3[:i] == s1[:i] else False
        for j in range(1, len(s2) + 1):
            dp[j][0] = True if s3[:j] == s2[:j] else False
        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s2[i-1]) or (dp[i][j-1] and s3[i+j-1] == s1[j-1])
        return dp[len(s2)][len(s1)]



if __name__ == '__main__':
    print(Solution().isInterleave( s1 = "db", s2 = "b", s3 = "cbb"))
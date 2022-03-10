
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
        for i in range(len(s)+1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and (dp[i+1][j-1] or abs(i-j) == 1):
                    dp[i][j] = 1
        return sum([j for i in dp for j in i])


if __name__ == '__main__':
    print(Solution().countSubstrings(s = "abc"))
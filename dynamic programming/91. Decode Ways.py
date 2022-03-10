class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) <= 1:
            if int(s) > 0:
                return 1
            return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1 if int(s[0]) > 0 else 0
        if dp[0] == 0:
            return 0
        dp[1] = 1
        if 0 < int(s[0:2]) <= 26:
            dp[1] += 1
        if int(s[1]) == 0:
            dp[1] -= 1
        for i in range(1, len(s)+1):
            dp[i] = dp[i-1] if s[i-1] != '0' else 0
            if (s[i-2] == '1') or (s[i-2] == '2' and 0 <= int(s[i-1]) <= 6):
                dp[i] += dp[i-2]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numDecodings("2611055971756562"))

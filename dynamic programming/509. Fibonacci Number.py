class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

if __name__ == '__main__':
    print(Solution().fib(21))
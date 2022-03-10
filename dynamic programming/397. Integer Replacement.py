class Solution:
    def integerReplacement1(self, n: int) -> int:
        # 动态规划，time limit exceeded
        dp = [0] * (n+1)
        for i in range(1, n+1):
            if i % 2 == 0:
                dp[i] = min(dp[i//2], dp[i-1]) + 1
            else:
                dp[i] = min(dp[i-1], dp[i//2+1]+1) + 1
        return dp[-1] - 1

    def integerReplacement(self, n: int) -> int:
        # 贪婪
        cnt = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                last, next = n-1, n+1
                l_cnt = 0
                while last % 2 == 0:
                    last /= 2
                    l_cnt +=1
                n_cnt = 0
                while next % 2 == 0:
                    next /= 2
                    n_cnt += 1
                n = n + 1 if n_cnt > l_cnt else n-1
            cnt += 1
        return cnt




if __name__ == '__main__':
    print(Solution().integerReplacement(1234))
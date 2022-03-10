from typing import List


class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0]*(amount+1)
        for i in coins:
            if i <= len(dp)-1:
                dp[i] = 1
        for i in range(1, amount+1):
            res = []
            for j in coins:
                if i - j >= 0 and dp[i-j] > 0:
                    res.append(dp[i-j]+1)
            if len(res) > 0:
                dp[i] = min(res)
        return dp[-1] if dp[-1] > 0 else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1] if dp[-1] <= amount else -1


if __name__ == '__main__':
    print(Solution().coinChange(coins = [2147483647], amount = 2))
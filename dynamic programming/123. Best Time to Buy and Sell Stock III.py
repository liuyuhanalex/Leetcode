from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        dp2 = [0 for _ in range(len(prices))]
        min_prices = prices[0]
        max_prices = prices[-1]
        for i in range(len(prices)-1):
            dp[i] = max(dp[i-1], prices[i] - min_prices)
            if prices[i] < min_prices:
                min_prices = prices[i]
        for i in range(len(prices)-2, -1, -1):
            dp2[i] = max(dp2[i+1], max_prices - prices[i])
            if prices[i] > max_prices:
                max_prices = prices[i]
        dp3 = [i+j for i, j in zip(dp, dp2)]
        return max(dp3)


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_1 = prices[0]
        max_price = 0
        for i in range(1, len(prices)):
            dp = min(dp_1, prices[i])
            dif = prices[i] - dp
            if dif > max_price:
                max_price = dif
            dp_1 = dp
        return max_price


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
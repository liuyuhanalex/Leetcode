from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass


if __name__ == '__main__':
    Solution().maxProfit([7, 1, 5, 3, 6, 4])
    # Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    # Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    # Total profit is 4 + 3 = 7.

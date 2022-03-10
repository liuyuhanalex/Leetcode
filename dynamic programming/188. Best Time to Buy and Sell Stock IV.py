from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        f = [[0 for _ in range(len(prices))] for _ in range(k)]
        g = [[0 for _ in range(len(prices))] for _ in range(k)]
        for i in range(k):
            for j in range(len(prices)):
                pass


if __name__ == '__main__':
    Solution().maxProfit(k = 2, prices = [3,2,6,5,0,3])
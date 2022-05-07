from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # dp[i] 为以i结尾的descent periods次数
        dp = [1 for _ in range(len(prices))]
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                dp[i] = dp[i] + dp[i-1]
        return sum(dp)




if __name__ == '__main__':
    print(Solution().getDescentPeriods(prices = [3,2,1,4]))
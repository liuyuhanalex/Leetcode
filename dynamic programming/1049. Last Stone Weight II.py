from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumweight = sum(stones)
        target = sumweight // 2
        dp = [0] * target
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sumweight - 2 * dp[target]


if __name__ == '__main__':
    print(Solution().lastStoneWeightII([31,26,33,21,40]))


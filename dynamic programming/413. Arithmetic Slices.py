from typing import List
import numpy as np


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # dp[i]的含义为 到i为止的等差数列数量
        if len(nums) < 3:
            return 0
        dp = np.zeros(len(nums))
        sum = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                sum += dp[i]
        return int(sum)


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([2, 1, 3, 4, 2, 3]))

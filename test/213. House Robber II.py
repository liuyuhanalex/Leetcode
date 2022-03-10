from typing import List
import numpy as np


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return int(max(nums))
        dp = np.zeros(len(nums)-1)
        # 两种情况，max(偷首不偷尾，偷尾不偷首)
        dp[0] = nums[0]
        for i in range(1, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        dp_2 = np.zeros(len(nums))
        dp_2[1] = nums[1]
        for i in range(2, len(nums)):
            dp_2[i] = max(dp_2[i-1], dp_2[i-2]+nums[i])
        return int(max(dp[-1], dp_2[-1]))


if __name__ == '__main__':
    print(Solution().rob(nums=[1, 2, 3]))

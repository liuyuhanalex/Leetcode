from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [0] * (len(nums)-1)
        dp[0] = nums[0]
        for i in range(1, len(nums) - 1):
            dp[i] = max(dp[i-1]-1, nums[i]) if dp[i-1]!= 0 else 0
        return dp[-1] > 0


if __name__ == '__main__':
    Solution().canJump([2, 3, 1, 1, 4])

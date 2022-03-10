from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # 最大绝对值可能是最大正数或者最小负数
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        max_pos = max(dp)
        for i in range(1, len(nums)):
            dp[i] = min(dp[i-1]+nums[i], nums[i])
        min_neg = min(dp)
        return max(abs(min_neg), abs(max_pos))



if __name__ == '__main__':
    print(Solution().maxAbsoluteSum([2,-5,1,-4,3,-2]))
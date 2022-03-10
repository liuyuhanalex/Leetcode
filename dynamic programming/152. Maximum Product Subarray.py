from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp数组的含义为以该数字结尾的最大的乘积
        # 分别记录最大的正数和最小的负数
        if len(nums) == 1:
            return nums[0]
        dp = [[0, 0] for _ in range(len(nums))]
        if nums[0] > 0:
            dp[0] = [nums[0], 0]
        else:
            dp[0] = [0, nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[i][0] = max(nums[i], dp[i-1][0]*nums[i])
                dp[i][1] = dp[i-1][1] * nums[i]
            else:
                dp[i][0] = dp[i-1][1] * nums[i]
                dp[i][1] = min(nums[i], nums[i] * dp[i-1][0])
        res = [i[0] for i in dp]
        return max(res)

if __name__ == '__main__':
    Solution().maxProduct(nums = [2, 3, -2, 4])
    print(Solution().maxProduct([7, -2, -4]))
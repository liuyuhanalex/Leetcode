from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
        dp = [0 for _ in range(len(nums))]
        for index, num in enumerate(nums):
            res = [0]
            for i in range(index-1, -2, -1):
                if nums[index] > nums[i]:
                    res.append(dp[i])
            dp[index] = max(res) + 1
        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))

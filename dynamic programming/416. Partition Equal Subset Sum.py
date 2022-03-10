from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        part_sum = total_sum // 2
        dp = [[-1 for _ in range(part_sum+1)] for _ in range(len(nums)+1)]
        dp[0] = [False for _ in range(len(dp[0]))]
        for i in range(len(nums)):
            dp[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, part_sum+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[len(nums)][part_sum]


if __name__ == '__main__':
    print(Solution().canPartition(nums=[14, 9, 8, 4, 3, 2]))


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1 if i in nums else 0 for i in range(target+1)]
        for i in range(1, target+1):
            for j in nums:
                if i-j > 0:
                    dp[i] += dp[i-j]
        return dp[-1]


if __name__ == '__main__':
    Solution().combinationSum4([1,2,3], 4)
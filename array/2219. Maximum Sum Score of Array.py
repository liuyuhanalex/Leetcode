from typing import List


class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        prefix_sum = 0
        total_sum = sum(nums)
        max_sum = 0
        for i in nums:
            prefix_sum += i
            max_sum = max(max_sum, prefix_sum, total_sum - prefix_sum + i)
        return max_sum



if __name__ == '__main__':
    print(Solution().maximumSumScore(nums = [4,3,-2,5]))
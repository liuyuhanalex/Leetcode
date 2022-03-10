from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        for i in range(k):
            sorted_nums = sorted(sorted_nums)
            sorted_nums[0] = 0 - sorted_nums[0]
        return sum(sorted_nums)


if __name__ == '__main__':
    print(Solution().largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))

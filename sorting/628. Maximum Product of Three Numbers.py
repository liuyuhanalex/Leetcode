from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        return max(sorted_nums[0]*sorted_nums[1]*sorted_nums[2], sorted_nums[-1]*sorted_nums[-2]*sorted_nums[0])


if __name__ == '__main__':
    print(Solution().maximumProduct([1, 2, 3, 4]))
    print(Solution().maximumProduct([-1, -2, -3]))
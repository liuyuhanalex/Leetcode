from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0, count_1 = 0, 0
        for i in nums:
            if i == 0:
                count_0 += 1
            elif i == 1:
                count_1 += 1
            else:
                pass
        for index, num in enumerate(nums):
            if index < count_0:
                nums[index] = 0
            elif count_0 <= index < count_0 + count_1:
                nums[index] = 1
            else:
                nums[index] = 2


if __name__ == '__main__':
    Solution().sortColors(nums=[2, 0, 2, 1, 1, 0])

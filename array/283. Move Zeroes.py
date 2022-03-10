from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer1, pointer2 = 0, 0
        for i in range(len(nums)):
            if nums[pointer2] != 0:
                nums[pointer1] = nums[pointer2]
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2 += 1
        for i in range(pointer1, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    Solution().moveZeroes(nums=[4, 2, 4, 0, 0, 3, 0, 5, 1, 0])

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 0, 0
        while end < len(nums):
            if nums[end] == nums[start]:
                end += 1
            else:
                nums[start+1] = nums[end]
                start += 1
                end += 1
        return start


if __name__ == '__main__':
    print(Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
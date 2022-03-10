from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        start, end = 0, 1
        count = 1
        while end < len(nums):
            if nums[start] == nums[end]:
                if count < 2:
                    nums[start + 1] = nums[end]
                    start += 1
                end += 1
                count += 1
            else:
                nums[start+1] = nums[end]
                count = 1
                start += 1
                end += 1
        return start + 1


if __name__ == '__main__':
    Solution().removeDuplicates(nums=[1,1,1,2,2,3])
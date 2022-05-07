from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        pointer = 1
        last = nums[0]
        cnt = 0
        while pointer < len(nums):
            if nums[pointer-1] == nums[pointer]:
                pointer += 1
            else:
                i = pointer + 1
                while i < len(nums) and nums[i] == nums[i-1]:
                    i += 1
                if i < len(nums):
                    if nums[pointer] > last and nums[pointer] > nums[i] or nums[pointer] < last and nums[pointer] < nums[i]:
                        cnt += 1
                last = nums[i-1]
                pointer = i
        return cnt





if __name__ == '__main__':
    Solution().countHillValley(nums = [6,6,5,5,4,1])

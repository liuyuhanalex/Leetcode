from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        pointer = 0
        while pointer < len(sorted_nums) -1:
            if sorted_nums[pointer] == sorted_nums[pointer + 1]:
                return sorted_nums[pointer]
            else:
                pointer += 2


if __name__ == '__main__':
    print(Solution().findDuplicate([3,1,3,4,2]))

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            i = abs(i)
            if nums[i-1] > 0:
                nums[i-1] = 0 - nums[i-1]
            else:
                res.append(abs(i))
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res




if __name__ == '__main__':
    Solution().findErrorNums(nums = [1,2,2,4])
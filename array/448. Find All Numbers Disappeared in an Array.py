from typing import List


class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 不使用额外的空间
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] = -nums[abs(i)-1]
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i)
        return res




if __name__ == '__main__':
    Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
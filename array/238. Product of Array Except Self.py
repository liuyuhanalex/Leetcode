from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for i in nums]
        total_product = 1
        for i in nums:
            if i != 0:
                total_product *= i
        if nums.count(0) == 1:
            res = []
            for i in nums:
                if i != 0:
                    res.append(0)
                else:
                    res.append(total_product)
            return res
        return [int(total_product/i) for i in nums]


if __name__ == '__main__':
    print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))

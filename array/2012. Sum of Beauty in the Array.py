from typing import List
import sys


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        left, right = [0], [sys.maxsize]
        for i in range(len(nums)):
            if nums[i] > left[-1]:
                left.append(nums[i])
            else:
                left.append(left[-1])
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < right[-1]:
                right.append(nums[i])
            else:
                right.append(right[-1])
        right = right[::-1]
        res = 0
        for i in range(1, len(nums) - 1):
            if left[i] < nums[i] < right[i+1]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
            else:
                pass
        return res




if __name__ == '__main__':
    print(Solution().sumOfBeauties(nums=[2, 2, 6]))
    print(Solution().sumOfBeauties(nums=[1, 2, 3]))
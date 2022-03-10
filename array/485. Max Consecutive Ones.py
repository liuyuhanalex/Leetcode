from typing import List

class Solution:
    def findMaxConsecutiveOnes0(self, nums: List[int]) -> int:
        zero_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index.append(i)
        zero_index = [-1] + zero_index + [len(nums)]
        max_length = 0
        for i in range(1, len(zero_index)):
            length = zero_index[i] - zero_index[i-1] -1
            if length > max_length:
                max_length = length
        return max_length

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        last = -1
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                length = i - last - 1
                if length > max_length:
                    max_length = length
                last = i
        if len(nums) - last - 1 > max_length:
            max_length = len(nums) - last - 1
        return max_length


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        begin, end = 0, len(nums) - 1
        while begin < end:
            pivot = begin + (end-begin)//2
            if nums[pivot] < target:
                begin = pivot + 1
            elif nums[pivot] == target:
                end = pivot
            else:
                end = pivot - 1
        if nums[begin]!= target:
            return [-1, -1]
        start = begin
        flag = False
        while begin < len(nums)-1 and nums[begin] == target:
            flag = True
            begin += 1
        if nums[begin] == target:
            end = begin
        elif flag:
            end = begin - 1
        else:
            end = begin

        return [start, end]


if __name__ == '__main__':
    print(Solution().searchRange(nums=[2, 2],
                                 target=2))
from typing import List
from math import ceil


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        while start < end:
            mid = ceil((start + end)/2)
            if nums[mid] == target:
                return mid
            if mid - start <= 1 and end-mid <= 1:
                break
            elif target > nums[mid]:
                start = mid
            else:
                end = mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = left + ceil((right-left)/2)
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                left = pivot+1
            else:
                right = pivot-1
        return -1


if __name__ == '__main__':
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2))

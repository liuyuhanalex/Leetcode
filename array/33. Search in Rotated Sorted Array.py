from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            pivot = start + (end-start)//2
            if nums[pivot] >= nums[start]:
                if nums[start] <= target < nums[pivot]:
                    end = pivot - 1
                elif nums[pivot] == target:
                    return pivot
                else:
                    start = pivot + 1
            else:
                if nums[pivot] < target <= nums[end]:
                    start = pivot + 1
                elif nums[pivot] == target:
                    return pivot
                else:
                    end = pivot - 1
        if nums[start] != target:
            return -1
        return start






if __name__ == '__main__':
    print(Solution().search(nums=[3, 1], target=1))

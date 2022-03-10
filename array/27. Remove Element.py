from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                while nums[end] == val and end > start:
                    end -= 1
                nums[start] = nums[end]
                end -= 1
            start += 1
        return max(0, end+1)

    def removeElement2(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast <= len(nums)-1:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow


if __name__ == '__main__':
    print(Solution().removeElement2(nums=[3, 2, 2, 3], val=3))

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # 三角形两边之和大于第三边
        cnt = 0
        for i in range(len(nums)-2):
            if nums[i] > 0:
                for j in range(i+1, len(nums)-1):
                    if nums[j] > 0:

                        cnt += self.binary_search(nums[j+1:], nums[i] + nums[j])
        return cnt

    def binary_search(self, nums, number):
        # 找到小于number的数的位置
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= number:
                right = mid
            else:
                left = mid + 1
        return left




if __name__ == '__main__':
    print(Solution().triangleNumber(nums = [48,66,61,46,94,75]))
    print(Solution().triangleNumber(nums = [2,2,3,4]))
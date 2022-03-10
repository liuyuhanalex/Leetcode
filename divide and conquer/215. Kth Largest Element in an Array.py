from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = 0
        num1 = [i for i in nums if i < nums[pivot]]
        num2 = [i for i in nums if i >= nums[pivot]]
        if len(num2) == k:
            return nums[pivot]
        elif len(num2) < k:
            return self.findKthLargest(num1, k - len(num2))
        else:
            return self.findKthLargest(num2[1:], k)



if __name__ == '__main__':
    print(Solution().findKthLargest(nums = [2,1], k = 2))
    #print(Solution().findKthLargest([3,2,1,5,6,4], 2))
    #print(Solution().findKthLargest([99,99],1))
    #print(Solution().findKthLargest([3, 1, 2, 4], 2))
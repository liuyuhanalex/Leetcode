from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # 使用heap来进行
        heapify(nums)
        while k > 0:
            num = heappop(nums)
            heappush(nums, num+1)
            k -= 1
        total = 1
        for i in nums:
            total = total * i % (10**9 + 7)
        return total



if __name__ == '__main__':
    Solution().maximumProduct(nums = [6,3,3,2], k = 2)
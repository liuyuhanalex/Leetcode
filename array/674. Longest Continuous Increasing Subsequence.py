from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cnt = 0
        last = 1
        max_length = 0
        for i in nums:
            if i > last:
                cnt += 1
                if cnt > max_length:
                    max_length = cnt
            else:
                cnt = 1
            last = i
        return max_length




if __name__ == '__main__':
    print(Solution().findLengthOfLCIS(nums = [1,3,5,4,7]))
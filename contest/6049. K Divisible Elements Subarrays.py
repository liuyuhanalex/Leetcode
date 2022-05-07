from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        for i in range(len(nums)):
            if nums[i] % p == 0:
                nums[i] = str(nums[i]//p) + 'x'
        nums = [str(i) for i in nums]
        final_set = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                string = ' '.join(nums[i:j])
                if string.count('x') <= k:
                    final_set.add(string)
        return len(final_set)








if __name__ == '__main__':
    #print(Solution().countDistinct(nums = [2,3,3,2,2], k = 2, p = 2))
    #print(Solution().countDistinct(nums = [1,2,3,4], k = 4, p = 1))
    print(Solution().countDistinct([1,9,8,7,19], 1, 6))

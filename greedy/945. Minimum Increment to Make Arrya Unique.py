from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        sorted_array = sorted(nums)
        final_set = set()
        cnt = 0
        max_num = 0
        for i in sorted_array:
            if i not in final_set:
                max_num = i
            else:
                max_num += 1
                cnt += max_num - i
            final_set.add(max_num)
        return cnt





if __name__ == '__main__':
    Solution().minIncrementForUnique(nums = [3,2,1,2,1,7])
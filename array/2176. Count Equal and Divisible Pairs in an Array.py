from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hash_table = {}
        for index, num in enumerate(nums):
            hash_table.setdefault(num, []).append(index)
        cnt = 0
        for index in range(len(nums)):
            total_list = hash_table.get(nums[index])
            for i in total_list:
                if i != index and (i * index) % k == 0:
                    cnt += 1
            hash_table[nums[index]].remove(index)
        return cnt


if __name__ == '__main__':
    Solution().countPairs(nums = [3,1,2,2,2,1,3], k = 2)
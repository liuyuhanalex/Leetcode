from typing import List
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hash_table = {}
        max_length = 0
        pos_table = {}
        for index, i in enumerate(nums):
            hash_table[i] = hash_table.get(i, 0) + 1
            if pos_table.get(i) is None:
                pos_table[i] = [index, index]
            else:
                start, end = pos_table.get(i)
                pos_table[i] = [start, index]
            if hash_table[i] > max_length:
                max_length = hash_table[i]
        re_list = [k for k, v in hash_table.items() if v == max_length]
        return min([pos_table.get(i)[1] - pos_table.get(i)[0] + 1 for i in re_list])

if __name__ == '__main__':
    print(Solution().findShortestSubArray([1,2,2,3,1]))
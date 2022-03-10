from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res_set = set()
        hash_table = {}
        for i in nums:
            res_set.add(i)
            count = hash_table.get(i, 0) + 1
            if count == 3:
                res_set.remove(i)
            else:
                hash_table[i] = count
        return res_set.pop()




if __name__ == '__main__':
    Solution().singleNumber([0,1,0,1,0,1,99])

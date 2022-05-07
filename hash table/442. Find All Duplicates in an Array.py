from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        p_hash = {}
        for i in nums:
            p_hash[i] = p_hash.get(i, 0) + 1
        res = []
        for k, v in p_hash.items():
            if v == 2:
                res.append(k)
        return res


if __name__ == '__main__':
    print(Solution().findDuplicates(nums = [4,3,2,7,8,2,3,1]))
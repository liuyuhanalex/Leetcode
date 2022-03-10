from typing import List



class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        hash_table = {}
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        total_list = [nums1, nums2, nums3]
        for i in range(3):
            for j in total_list[i]:
                hash_table[j] = hash_table.get(j, 0 ) + 1
        res = []
        for k, v in hash_table.items():
            if v>=2:
                res.append(k)
        return res



if __name__ == '__main__':
    Solution().twoOutOfThree([1,2,2], nums2 = [4,3,3], nums3 = [5])
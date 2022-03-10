from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        for i in nums1:
            dict1[i] = dict1.get(i, 0) + 1
        dict2 = {}
        for i in nums2:
            dict2[i] = dict2.get(i, 0) + 1
        res = []
        for i in dict1.keys():
            if dict2.get(i) is not None:
                res = res + [i] * min(dict2.get(i), dict1.get(i))
        return res




if __name__ == '__main__':
    Solution().intersect(nums1 = [1,2,2,1], nums2 = [2,2])
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1, pointer2 = 0, 0
        res = []
        while pointer1 < m and pointer2 < n:
            if nums1[pointer1] < nums2[pointer2]:
                res.append(nums1[pointer1])
                pointer1 += 1
            else:
                res.append(nums2[pointer2])
                pointer2 += 1
        if pointer1 < m:
            res += nums1[pointer1: m]
        if pointer2 < n:
            res += nums2[pointer2:]
        for i in range(len(nums1)):
            nums1[i] = res[i]



if __name__ == '__main__':
    Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        hash1, hash2, hash3, hash4 = {}, {}, {}, {}
        for i1, i2, i3, i4 in zip(nums1, nums2, nums3, nums4):
            hash1[i1] = hash1.get(i1, 0) + 1
            hash2[i2] = hash2.get(i2, 0) + 1
            hash3[i3] = hash3.get(i3, 0) + 1
            hash4[i4] = hash4.get(i4, 0) + 1
        for i1 in hash1.keys():
            for i2 in hash2.keys():
                for i3 in hash3.keys():
                    for i4 in hash4.keys():
                        if i1 + i2 + i3 + i4 == 0:
                            cnt += hash1.get(i1) * hash2.get(i2) * hash3.get(i3) * hash4.get(i4)
        return cnt

if __name__ == '__main__':
    print(Solution().fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
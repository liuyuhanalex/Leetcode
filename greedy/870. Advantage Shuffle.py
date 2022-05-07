from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        final = []
        for i in nums2:
            right, left = 0, len(nums1)
            while right < left:
                mid = right + (left - right) // 2
                if nums1[mid] <= i:
                    right = mid + 1
                else:
                    left = mid
            if left < len(nums1):
                final.append(nums1[left])
                nums1.pop(left)
            else:
                final.append(nums1[0])
                nums1.pop(0)
        return final


if __name__ == '__main__':
    #print(Solution().advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]))
    print(Solution().advantageCount([12,24,8,32], [13,25,32,11]))
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_table = {}
        for index, i in enumerate(nums2):
            if not stack:
                stack.append(index)
            else:
                while len(stack) > 0 and nums2[stack[-1]] < i:
                    old_index = stack.pop()
                    if nums2[old_index] in nums1:
                        hash_table[nums2[old_index]] = i
                stack.append(index)
        res = []
        for i in nums1:
            res.append(hash_table.get(i, -1))
        return res



if __name__ == '__main__':
    Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])

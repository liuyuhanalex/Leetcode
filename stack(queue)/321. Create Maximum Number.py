from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = []
        for i in range(min(len(nums1) + 1, k + 1)):
            len_nums2 = k - i
            if len(nums2) >= len_nums2:
                # 从nums1 中取i个，从nums2中取k-i个
                list1 = self.get_max_arrangement(nums1, i)
                list2 = self.get_max_arrangement(nums2, len_nums2)
                p1, p2 = 0, 0
                final_list = []
                while p1 < len(list1) or p2 < len(list2):
                    if list1[p1:] > list2[p2:]:
                        final_list.append(list1[p1])
                        p1 += 1
                    else:
                        final_list.append(list2[p2])
                        p2 += 1
                str_1 = ''.join([str(i) for i in final_list])
                res.append(str_1)
        max_num = max(res)
        res = [int(i) for i in list(str(max_num))]
        return res

    def get_max_arrangement(self, num_list: List[int], count: int):
        if count == 0:
            return []
        stack = []
        cnt = 0
        for i in num_list:
            if stack:
                while stack and cnt < len(num_list) - count and i > stack[-1]:
                    stack.pop()
                    cnt += 1
                stack.append(i)
            else:
                stack.append(i)
        while cnt < len(num_list) - count:
            stack.pop()
            cnt += 1
        return stack

if __name__ == '__main__':
    #print(Solution().maxNumber([5,2,2], [6,4,1] , 3))
    #print(Solution().maxNumber([3,4,6,5], [9,1,2,5,8,3], 5))
    print(Solution().maxNumber([9,1,2,5,8,3], [3,4,6,5], 5))
    #print(Solution().get_max_arrangement([5,2,2], 1))
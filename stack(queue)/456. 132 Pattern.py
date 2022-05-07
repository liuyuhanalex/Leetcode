from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second_num = -10000000
        for i in reversed(nums):
            if i < second_num:
                return True
            if not stack or i < stack[-1]:
                stack.append(i)
            else:
                while stack and i > stack[-1]:
                    second_num = stack.pop()
                stack.append(i)
        return False





if __name__ == '__main__':
    print(Solution().find132pattern(nums = [3,1,4,2]))
    #print(Solution().find132pattern([1,0,1,-4,-3]))
    #print(Solution().find132pattern([1,0,1,-4,-3]))
    #print(Solution().find132pattern([-2, 1, -1]))
    #print(Solution().find132pattern([3, 5, 0, 3, 4]))
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(heights)):
            if not stack or heights[i] < heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] <= heights[i]:
                    index = stack.pop()
                    res.append(index)
                stack.append(i)
        return stack



if __name__ == '__main__':
    #Solution().findBuildings(heights = [4,2,3,1])
    print(Solution().findBuildings([1, 3, 2, 4]))
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])
        stack = []
        for i in sorted_points:
            if not stack:
                stack.append(i)
            else:
                if i[0] <= stack[-1][1]:
                    last = stack.pop()
                    stack.append([max(last[0], i[0]), min(last[1], i[1])])
                else:
                    stack.append(i)
        return len(stack)




if __name__ == '__main__':
    Solution().findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]])
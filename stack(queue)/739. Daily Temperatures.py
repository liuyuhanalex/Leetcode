from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for index, i in enumerate(temperatures):
            if not stack:
                stack.append(index)
            else:
                while len(stack) > 0 and temperatures[stack[-1]] < i:
                    old_index = stack.pop(-1)
                    res[old_index] = index - old_index
                stack.append(index)
        return res




if __name__ == '__main__':
    Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
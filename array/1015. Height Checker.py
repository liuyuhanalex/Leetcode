from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        count = 0
        for i, j in zip(heights, sorted_height):
            if i != j:
                count += 1
        return count

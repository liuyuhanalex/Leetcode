from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high_al = 0
        sum_hi = 0
        for i in gain:
            sum_hi += i
            if sum_hi > high_al:
                high_al = sum_hi
        return high_al


if __name__ == '__main__':
    print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))
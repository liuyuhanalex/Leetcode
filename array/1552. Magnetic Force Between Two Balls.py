from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        sorted_list = sorted(position)
        print(sorted_list)



if __name__ == '__main__':
    Solution().maxDistance(position = [1,2,3,4,7], m = 3)
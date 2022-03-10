from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res_dict = {}
        for index, value in enumerate(nums):
            res_val = res_dict.get(value)
            if res_val is not None and index - res_val <= k:
                return True
            res_dict[value] = index
        return False




if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))

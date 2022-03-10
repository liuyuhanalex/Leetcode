from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_num = sum(arr)
        if sum_num % 3 != 0:
            return False
        part_num = sum_num // 3
        prefix_sum = 0
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum == part_num:
                second_prefix = 0
                for j in range(i+1, len(arr)-1):
                    second_prefix += arr[j]
                    if second_prefix == part_num:
                        return True
        return False





if __name__ == '__main__':
    Solution().canThreePartsEqualSum(arr = [3,3,6,5,-2,2,5,1,-9,4])